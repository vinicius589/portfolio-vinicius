"""Cena 3D: um caracol robotico encontra um onibus de brinquedo."""

import math
from pathlib import Path

import pygame

from py3d.core.base import Base
from py3d.core_ext.renderer import Renderer
from py3d.core_ext.scene import Scene
from py3d.core_ext.camera import Camera
from py3d.core_ext.mesh import Mesh
from py3d.core_ext.group import Group
from py3d.core_ext.texture import Texture
from py3d.light.ambient import AmbientLight
from py3d.light.directional import DirectionalLight
from py3d.material.phong import PhongMaterial
from py3d.geometry.box import BoxGeometry
from py3d.geometry.sphere import SphereGeometry
from py3d.geometry.ellipsoid import EllipsoidGeometry
from py3d.geometry.cylinder import CylinderGeometry
from py3d.geometry.rectangle import RectangleGeometry
from py3d.extras.movement_rig import MovementRig

from animacao import SequenciaAnimacao


PASTA_PROJETO = Path(__file__).resolve().parent
PASTA_ASSETS = PASTA_PROJETO / "assets"


class TrabalhoComputacaoGrafica(Base):
    """Monta a cena, controla a animacao e desenha cada quadro."""

    def __init__(self):
        super().__init__(screen_size=(1100, 720))

    def criar_material(self, cor, textura=None):
        """Cria um material Phong com iluminacao e suporte a sombras."""
        return PhongMaterial(
            texture=textura,
            number_of_light_sources=2,
            use_shadow=True,
            property_dict={"baseColor": cor}
        )

    def adicionar_peca(self, grupo, geometria, material, posicao):
        """Cria uma malha, posiciona e adiciona ao grupo informado."""
        peca = Mesh(geometria, material)
        peca.set_position(posicao)
        grupo.add(peca)
        return peca

    def initialize(self):
        pygame.display.set_caption("Caracol Robotico e Onibus - Computacao Grafica")

        # Renderizador, cena e camera em perspectiva.
        self.renderer = Renderer(clear_color=(0.34, 0.52, 0.68))
        self.scene = Scene()
        self.camera = Camera(angle_of_view=55, aspect_ratio=1100 / 720, near=0.1, far=100)
        self.camera.set_position([8, 7, 11])
        self.camera.look_at([0, 0.8, 0])

        # O rig permite mover e orientar a camera pelo teclado.
        self.camera_rig = MovementRig(units_per_second=4, degrees_per_second=65)
        self.camera_rig.add(self.camera)
        self.scene.add(self.camera_rig)

        # Iluminacao ambiente e luz direcional.
        luz_ambiente = AmbientLight(color=[0.38, 0.38, 0.42])
        luz_direcional = DirectionalLight(color=[0.95, 0.90, 0.82])
        luz_direcional.set_position([5, 10, 6])
        luz_direcional.set_direction([-0.45, -1.0, -0.55])
        self.scene.add(luz_ambiente)
        self.scene.add(luz_direcional)

        # A sombra e calculada pelo mapa de profundidade do framework.
        self.renderer.enable_shadows(luz_direcional, strength=0.58, resolution=(1024, 1024))
        # Aumenta a area vista pela camera da luz para cobrir toda a cena.
        self.renderer.shadow_object.camera.set_orthographic(
            left=-8, right=8, bottom=-8, top=8, near=0, far=28
        )

        # Materiais usados pelos objetos da cena.
        self.material_asfalto = self.criar_material(
            [0.78, 0.80, 0.82], Texture(str(PASTA_ASSETS / "asfalto.png"))
        )
        self.material_cinza = self.criar_material([0.22, 0.25, 0.29])
        self.material_branco = self.criar_material([0.92, 0.92, 0.88])
        self.material_amarelo = self.criar_material([0.95, 0.67, 0.12])
        self.material_azul = self.criar_material([0.08, 0.35, 0.72])
        self.material_vidro = self.criar_material([0.25, 0.72, 0.88])
        self.material_pneu = self.criar_material([0.035, 0.04, 0.05])
        self.material_metal = self.criar_material([0.52, 0.57, 0.62])
        self.material_verde = self.criar_material([0.18, 0.62, 0.43])
        self.material_casco = self.criar_material([0.72, 0.34, 0.13])
        self.material_antena = self.criar_material([0.90, 0.78, 0.30])
        self.material_luz = self.criar_material([1.0, 0.83, 0.28])

        self.criar_ambiente()
        self.criar_onibus()
        self.criar_caracol()

        # Estado inicial da animacao.
        self.animacao = SequenciaAnimacao()
        self.tempo_cena = 0.0
        self.pausado = False
        self.angulo_antena = 0.0

    def criar_ambiente(self):
        """Cria o chao texturizado, faixa de pedestres e ponto de onibus."""
        chao = self.adicionar_peca(
            self.scene,
            RectangleGeometry(width=24, height=22),
            self.material_asfalto,
            [0, 0, 0]
        )
        chao.rotate_x(-math.pi / 2)

        # Calcada ao lado do ponto.
        self.adicionar_peca(
            self.scene, BoxGeometry(3.0, 0.18, 8.0), self.material_cinza,
            [2.8, 0.02, 0.8]
        )

        # Faixas brancas da travessia.
        for indice in range(6):
            self.adicionar_peca(
                self.scene, BoxGeometry(0.48, 0.025, 2.8), self.material_branco,
                [0.6 + indice * 0.58, 0.025, -2.5]
            )

        # Poste e placa do ponto de onibus.
        self.adicionar_peca(
            self.scene, CylinderGeometry(radius=0.055, height=2.1), self.material_metal,
            [1.25, 1.15, 2.6]
        )
        self.adicionar_peca(
            self.scene, BoxGeometry(0.85, 0.85, 0.12), self.material_azul,
            [1.25, 2.25, 2.6]
        )
        self.adicionar_peca(
            self.scene, BoxGeometry(0.28, 0.42, 0.04), self.material_branco,
            [1.25, 2.25, 2.51]
        )

        # Banco simples para deixar o ambiente reconhecivel.
        self.adicionar_peca(
            self.scene, BoxGeometry(1.6, 0.12, 0.42), self.material_amarelo,
            [1.65, 0.62, 0.95]
        )
        self.adicionar_peca(
            self.scene, BoxGeometry(1.6, 0.72, 0.12), self.material_metal,
            [1.65, 1.0, 1.12]
        )
        for pos_x in [1.05, 2.25]:
            self.adicionar_peca(
                self.scene, BoxGeometry(0.10, 0.42, 0.10), self.material_metal,
                [pos_x, 0.34, 0.95]
            )

    def criar_onibus(self):
        """Monta o onibus com caixas, rodas, janelas e uma porta movel."""
        self.onibus = Group()
        self.scene.add(self.onibus)

        # Parte inferior e carroceria.
        self.adicionar_peca(
            self.onibus, BoxGeometry(2.0, 0.58, 3.8), self.material_amarelo,
            [0, 0.62, 0]
        )
        self.adicionar_peca(
            self.onibus, BoxGeometry(1.92, 1.18, 3.2), self.material_amarelo,
            [0, 1.38, 0.1]
        )
        self.adicionar_peca(
            self.onibus, BoxGeometry(1.82, 0.12, 3.25), self.material_azul,
            [0, 2.03, 0.1]
        )

        # Para-brisa dianteiro e vidro traseiro.
        self.adicionar_peca(
            self.onibus, BoxGeometry(1.25, 0.58, 0.045), self.material_vidro,
            [0, 1.53, -1.52]
        )
        self.adicionar_peca(
            self.onibus, BoxGeometry(1.25, 0.52, 0.045), self.material_vidro,
            [0, 1.50, 1.72]
        )

        # Janelas laterais. No lado da porta, deixamos livre o espaco
        # para ela deslizar para tras quando abrir.
        for lado in [-1, 1]:
            for pos_z in [-1.0, 0.0, 1.1]:
                if lado == 1 and pos_z in [0.0, 1.1]:
                    continue
                self.adicionar_peca(
                    self.onibus, BoxGeometry(0.045, 0.52, 0.72), self.material_vidro,
                    [lado * 0.98, 1.55, pos_z]
                )

        # Fundo escuro para mostrar o vao quando a porta desliza.
        self.adicionar_peca(
            self.onibus, BoxGeometry(0.04, 0.90, 0.80), self.material_cinza,
            [1.005, 1.05, -0.05]
        )

        # Porta lateral: desloca para tras no eixo Z para abrir.
        self.porta_onibus = self.adicionar_peca(
            self.onibus, BoxGeometry(0.055, 0.88, 0.78), self.material_azul,
            [1.02, 1.05, -0.05]
        )

        # Rodas. Primeiro deitamos o cilindro com uma rotacao em Z.
        # A rotacao em Y feita depois gira a roda em torno do proprio eixo.
        self.rodas = []
        for lado in [-1, 1]:
            for pos_z in [-1.25, 1.25]:
                roda = self.adicionar_peca(
                    self.onibus, CylinderGeometry(radius=0.36, height=0.18), self.material_pneu,
                    [lado * 1.02, 0.38, pos_z]
                )
                roda.rotate_z(math.pi / 2)
                self.rodas.append(roda)

                cubo_roda = self.adicionar_peca(
                    self.onibus, CylinderGeometry(radius=0.16, height=0.20), self.material_metal,
                    [lado * 1.02, 0.38, pos_z]
                )
                cubo_roda.rotate_z(math.pi / 2)
                self.rodas.append(cubo_roda)

        # Farois frontais e lanternas traseiras.
        for lado in [-1, 1]:
            self.adicionar_peca(
                self.onibus, SphereGeometry(radius=0.13), self.material_luz,
                [lado * 0.68, 0.68, -1.94]
            )
            self.adicionar_peca(
                self.onibus, BoxGeometry(0.22, 0.22, 0.08), self.material_cinza,
                [lado * 0.68, 0.68, 1.94]
            )

    def criar_antena(self, grupo, posicao):
        """Cria uma antena articulada com uma pequena esfera na ponta."""
        antena = Group()
        antena.set_position(posicao)
        grupo.add(antena)

        self.adicionar_peca(
            antena, CylinderGeometry(radius=0.045, height=0.48), self.material_antena,
            [0, 0.24, 0]
        )
        self.adicionar_peca(
            antena, SphereGeometry(radius=0.13), self.material_luz,
            [0, 0.49, 0]
        )
        return antena

    def criar_caracol(self):
        """Monta o caracol com corpo, casco e duas antenas articuladas."""
        self.caracol = Group()
        self.caracol.rotate_y(math.pi)
        self.scene.add(self.caracol)

        # Corpo alongado e cabeca arredondada.
        self.adicionar_peca(
            self.caracol, EllipsoidGeometry(1.55, 0.62, 0.62), self.material_verde,
            [0, 0.43, 0]
        )
        self.adicionar_peca(
            self.caracol, EllipsoidGeometry(0.72, 0.72, 0.66), self.material_verde,
            [0.64, 0.67, 0]
        )

        # Casco grande, feito com uma esfera achatada.
        self.adicionar_peca(
            self.caracol, EllipsoidGeometry(1.10, 1.18, 1.00), self.material_casco,
            [-0.18, 0.93, 0]
        )

        # Pequeno sensor no casco; a escala reduz o tamanho da esfera.
        sensor = self.adicionar_peca(
            self.caracol, SphereGeometry(radius=0.22), self.material_antena,
            [-0.18, 0.94, 0.52]
        )
        sensor.scale(0.75)

        # Antenas independentes para que possam balancar.
        self.antena_esquerda = self.criar_antena(self.caracol, [0.82, 1.02, -0.22])
        self.antena_direita = self.criar_antena(self.caracol, [0.82, 1.02, 0.22])

    def update(self):
        # A barra de espaco pausa e retoma somente a animacao dos personagens.
        if self.input.is_key_down("space"):
            self.pausado = not self.pausado

        # A camera continua podendo ser movimentada mesmo com a animacao pausada.
        self.camera_rig.update(self.input, self.delta_time)

        if not self.pausado:
            self.animacao.atualizar(self.delta_time)
            self.tempo_cena += self.delta_time

        # Posicoes calculadas pelo controlador de animacao.
        self.onibus.set_position([-2.3, 0, self.animacao.z_onibus])
        self.caracol.set_position([self.animacao.x_caracol, 0, 1.0])

        # A porta desliza para tras para liberar a entrada do onibus.
        self.porta_onibus.set_position([1.02, 1.05, -0.05 + self.animacao.porta * 0.84])

        # As rodas so giram quando o onibus realmente esta se deslocando.
        if not self.pausado and self.animacao.onibus_esta_se_movendo():
            for roda in self.rodas:
                roda.rotate_y(-5.0 * self.delta_time)

        # As antenas balancam com mais intensidade durante a sinalizacao.
        intensidade = 0.30 if self.animacao.etapa == "sinalizar" else 0.08
        novo_angulo = math.sin(self.tempo_cena * 5.0) * intensidade
        diferenca = novo_angulo - self.angulo_antena
        self.antena_esquerda.rotate_z(diferenca)
        self.antena_direita.rotate_z(-diferenca)
        self.angulo_antena = novo_angulo

        # Desenha a cena, incluindo a passagem de shadow mapping.
        self.renderer.render(self.scene, self.camera)


if __name__ == "__main__":
    TrabalhoComputacaoGrafica().run()
