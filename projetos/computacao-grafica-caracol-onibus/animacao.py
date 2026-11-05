"""Controle simples da sequencia entre o caracol robotico e o onibus."""


class SequenciaAnimacao:
    """Calcula posicoes e etapas usando o tempo decorrido, em segundos."""

    def __init__(self):
        self.reiniciar()

    def reiniciar(self):
        # Posicoes iniciais dos dois personagens.
        self.x_caracol = 3.6
        self.z_onibus = 6.0

        # 0 = porta fechada; 1 = porta aberta.
        self.porta = 0.0

        # Etapas: aproximacao, abrir, sinalizar, fechar, partir e espera.
        self.etapa = "aproximacao"
        self.tempo_etapa = 0.0

    def onibus_esta_se_movendo(self):
        """Informa se as rodas devem girar nesta etapa."""
        if self.etapa == "aproximacao":
            return self.z_onibus > 1.2

        if self.etapa == "partir":
            return self.z_onibus > -6.0

        return False

    def atualizar(self, delta_tempo):
        """Atualiza a cena sem depender da quantidade de quadros por segundo."""
        if delta_tempo <= 0:
            return

        if self.etapa == "aproximacao":
            # O caracol vai ate o ponto e o onibus se aproxima da parada.
            self.x_caracol = max(0.25, self.x_caracol - 1.0 * delta_tempo)
            self.z_onibus = max(1.2, self.z_onibus - 2.0 * delta_tempo)

            # A proxima acao so comeca quando os dois chegam.
            if self.x_caracol <= 0.25 and self.z_onibus <= 1.2:
                self.etapa = "abrir"
                self.tempo_etapa = 0.0

        elif self.etapa == "abrir":
            # A porta abre gradualmente durante 0,8 segundo.
            self.tempo_etapa += delta_tempo
            self.porta = min(1.0, self.tempo_etapa / 0.8)

            if self.tempo_etapa >= 0.8:
                self.etapa = "sinalizar"
                self.tempo_etapa = 0.0

        elif self.etapa == "sinalizar":
            # O caracol movimenta as antenas enquanto o onibus espera.
            self.tempo_etapa += delta_tempo

            if self.tempo_etapa >= 1.8:
                self.etapa = "fechar"
                self.tempo_etapa = 0.0

        elif self.etapa == "fechar":
            # A porta fecha antes de o onibus sair.
            self.tempo_etapa += delta_tempo
            self.porta = max(0.0, 1.0 - self.tempo_etapa / 0.8)

            if self.tempo_etapa >= 0.8:
                self.etapa = "partir"
                self.tempo_etapa = 0.0

        elif self.etapa == "partir":
            # O onibus so parte depois que a porta termina de fechar.
            self.z_onibus -= 2.4 * delta_tempo

            if self.z_onibus <= -6.0:
                self.etapa = "espera"
                self.tempo_etapa = 0.0

        elif self.etapa == "espera":
            # Pequena pausa antes de repetir a demonstracao.
            self.tempo_etapa += delta_tempo

            if self.tempo_etapa >= 1.0:
                self.reiniciar()
