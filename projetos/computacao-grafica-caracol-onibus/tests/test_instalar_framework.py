"""Testes do instalador sem precisar acessar a internet."""

from io import BytesIO
from zipfile import BadZipFile, ZipFile

import instalar_framework


def criar_zip_de_teste():
    """Monta um ZIP pequeno com a estrutura esperada do framework."""
    dados = BytesIO()
    with ZipFile(dados, "w") as pacote:
        pacote.writestr("repositorio/py3d/__init__.py", "")
        pacote.writestr("repositorio/py3d/core/base.py", "# Base")
        pacote.writestr("repositorio/py3d/core_ext/renderer.py", "# Renderer")
        pacote.writestr("repositorio/py3d/material/phong.py", "# Phong")
        pacote.writestr("repositorio/py3d/material/depth.py", "# Depth")
        pacote.writestr("repositorio/README.md", "arquivo que nao deve ser extraido")
    dados.seek(0)
    return dados


def test_framework_valido_identifica_pasta_completa(tmp_path):
    pasta = tmp_path / "py3d"
    (pasta / "core").mkdir(parents=True)
    (pasta / "core_ext").mkdir()
    (pasta / "material").mkdir()

    arquivos = [
        "__init__.py",
        "core/base.py",
        "core_ext/renderer.py",
        "material/phong.py",
        "material/depth.py",
    ]
    for nome in arquivos:
        (pasta / nome).write_text("", encoding="utf-8")

    assert instalar_framework.framework_valido(pasta) is True


def test_extrair_framework_copia_somente_a_pasta_py3d(tmp_path, monkeypatch):
    destino = tmp_path / "py3d"
    temporaria = tmp_path / "py3d_temp"
    monkeypatch.setattr(instalar_framework, "DESTINO", destino)
    monkeypatch.setattr(instalar_framework, "TEMPORARIA", temporaria)

    instalar_framework.extrair_framework(criar_zip_de_teste())

    assert instalar_framework.framework_valido(destino) is True
    assert (destino / "core" / "base.py").read_text(encoding="utf-8") == "# Base"
    assert not (destino / "README.md").exists()
    assert not temporaria.exists()


def test_zip_sem_framework_e_rejeitado(tmp_path, monkeypatch):
    destino = tmp_path / "py3d"
    temporaria = tmp_path / "py3d_temp"
    monkeypatch.setattr(instalar_framework, "DESTINO", destino)
    monkeypatch.setattr(instalar_framework, "TEMPORARIA", temporaria)

    dados = BytesIO()
    with ZipFile(dados, "w") as pacote:
        pacote.writestr("outro_arquivo.txt", "sem framework")
    dados.seek(0)

    try:
        instalar_framework.extrair_framework(dados)
        assert False, "Era esperado um erro de ZIP sem a pasta py3d."
    except BadZipFile:
        assert not destino.exists()
