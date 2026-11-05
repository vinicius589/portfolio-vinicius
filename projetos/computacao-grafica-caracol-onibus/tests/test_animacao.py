"""Testes da sequencia de animacao sem precisar abrir uma janela 3D."""

from animacao import SequenciaAnimacao


def avancar_ate(animacao, etapa, limite=2000, passo=0.05):
    """Avanca o tempo ate a etapa informada, ou falha se nao chegar."""
    for _ in range(limite):
        if animacao.etapa == etapa:
            return
        animacao.atualizar(passo)
    raise AssertionError(f"A animacao nao chegou a etapa: {etapa}")


def test_onibus_e_caracol_precisam_chegar_antes_da_porta_abrir():
    animacao = SequenciaAnimacao()
    avancar_ate(animacao, "abrir")
    assert animacao.x_caracol == 0.25
    assert animacao.z_onibus == 1.2
    assert animacao.porta == 0.0


def test_porta_abre_antes_da_sinalizacao():
    animacao = SequenciaAnimacao()
    avancar_ate(animacao, "sinalizar")
    assert animacao.porta == 1.0
    assert animacao.etapa == "sinalizar"


def test_onibus_so_parte_depois_de_fechar_a_porta():
    animacao = SequenciaAnimacao()
    avancar_ate(animacao, "partir")
    assert animacao.porta == 0.0
    assert animacao.z_onibus == 1.2
    animacao.atualizar(0.5)
    assert animacao.z_onibus < 1.2


def test_animacao_reinicia_apos_o_onibus_sair():
    animacao = SequenciaAnimacao()
    avancar_ate(animacao, "espera")
    animacao.atualizar(1.1)
    assert animacao.etapa == "aproximacao"
    assert animacao.x_caracol == 3.6
    assert animacao.z_onibus == 6.0


def test_delta_tempo_zero_nao_muda_a_cena():
    animacao = SequenciaAnimacao()
    posicao_inicial = (animacao.x_caracol, animacao.z_onibus, animacao.etapa)
    animacao.atualizar(0)
    assert (animacao.x_caracol, animacao.z_onibus, animacao.etapa) == posicao_inicial


def test_onibus_espera_enquanto_o_caracol_termina_de_chegar():
    animacao = SequenciaAnimacao()
    animacao.atualizar(2.5)
    assert animacao.etapa == "aproximacao"
    assert animacao.z_onibus == 1.2
    assert animacao.x_caracol > 0.25


def test_chegada_final_nao_depende_do_tamanho_do_passo():
    animacao_rapida = SequenciaAnimacao()
    animacao_lenta = SequenciaAnimacao()
    avancar_ate(animacao_rapida, "abrir", passo=0.01)
    avancar_ate(animacao_lenta, "abrir", passo=0.10)
    assert animacao_rapida.x_caracol == animacao_lenta.x_caracol == 0.25
    assert animacao_rapida.z_onibus == animacao_lenta.z_onibus == 1.2


def test_rodas_param_quando_o_onibus_espera_o_caracol():
    animacao = SequenciaAnimacao()
    animacao.atualizar(2.5)
    assert animacao.etapa == "aproximacao"
    assert animacao.z_onibus == 1.2
    assert animacao.onibus_esta_se_movendo() is False


def test_rodas_giram_durante_a_chegada_e_a_partida():
    animacao = SequenciaAnimacao()
    assert animacao.onibus_esta_se_movendo() is True
    avancar_ate(animacao, "partir")
    assert animacao.onibus_esta_se_movendo() is True
