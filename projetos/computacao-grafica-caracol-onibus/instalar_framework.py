"""Baixa e instala a pasta py3d do framework usado nos exemplos do livro."""

from io import BytesIO
from pathlib import Path
import shutil
import sys
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen
from zipfile import BadZipFile, ZipFile

PASTA_PROJETO = Path(__file__).resolve().parent
DESTINO = PASTA_PROJETO / "py3d"
TEMPORARIA = PASTA_PROJETO / "py3d_temp"
URL = (
    "https://codeload.github.com/ax-va/"
    "PyOpenGL-Pygame-Stemkoski-Pascale-2021/zip/"
    "f3029550425385f90e0d66ba7f73bb310112039b"
)


def framework_valido(pasta):
    """Confere se os arquivos principais do framework estao presentes."""
    arquivos = [
        pasta / "__init__.py",
        pasta / "core" / "base.py",
        pasta / "core_ext" / "renderer.py",
        pasta / "material" / "phong.py",
        pasta / "material" / "depth.py",
    ]
    return all(arquivo.is_file() for arquivo in arquivos)


def extrair_framework(dados_zip):
    """Extrai somente a pasta py3d, sem deixar uma instalacao pela metade."""
    if TEMPORARIA.exists():
        shutil.rmtree(TEMPORARIA)
    TEMPORARIA.mkdir(parents=True)

    with ZipFile(dados_zip) as pacote:
        erro = pacote.testzip()
        if erro:
            raise BadZipFile(f"Arquivo corrompido: {erro}")

        arquivos = pacote.namelist()
        arquivo_inicial = next(
            (nome for nome in arquivos if nome.endswith("/py3d/__init__.py")),
            None,
        )
        if arquivo_inicial is None:
            raise BadZipFile("A pasta py3d nao foi encontrada no arquivo baixado.")

        pasta_raiz = arquivo_inicial.rsplit("/py3d/__init__.py", 1)[0] + "/py3d/"

        for item in arquivos:
            if item.startswith(pasta_raiz) and not item.endswith("/"):
                caminho_relativo = item[len(pasta_raiz):]
                destino = TEMPORARIA / caminho_relativo
                destino.parent.mkdir(parents=True, exist_ok=True)
                with pacote.open(item) as origem, destino.open("wb") as saida:
                    shutil.copyfileobj(origem, saida)

    if not framework_valido(TEMPORARIA):
        raise BadZipFile("O framework baixado esta incompleto.")

    if DESTINO.exists():
        shutil.rmtree(DESTINO)
    TEMPORARIA.replace(DESTINO)


def main():
    """Verifica a instalacao e baixa o framework quando necessario."""
    if framework_valido(DESTINO):
        print("Framework Py3D ja esta instalado.")
        return 0

    if DESTINO.exists():
        print("Instalacao anterior incompleta. Corrigindo...")
        shutil.rmtree(DESTINO)

    print("Baixando o framework Py3D do repositorio de exemplos do livro...")

    try:
        requisicao = Request(
            URL,
            headers={"User-Agent": "Trabalho-Computacao-Grafica/1.0"},
        )
        with urlopen(requisicao, timeout=60) as resposta:
            dados_zip = BytesIO(resposta.read())

        extrair_framework(dados_zip)
        print("Framework instalado com sucesso na pasta py3d.")
        return 0

    except (HTTPError, URLError, TimeoutError, OSError, BadZipFile, StopIteration) as erro:
        if TEMPORARIA.exists():
            shutil.rmtree(TEMPORARIA)
        print("ERRO: nao foi possivel instalar o framework Py3D.")
        print(f"Detalhes: {erro}")
        print("Confira a internet e execute INICIAR.bat novamente.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
