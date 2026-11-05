# Caracol robótico e ônibus de brinquedo

Projeto acadêmico de Computação Gráfica da UNIPAC, desenvolvido em Python, Pygame, OpenGL e no framework Py3D associado ao livro de Lee Stemkoski e Michael Pascale.

## Cena

A cena mostra um caracol robótico que se aproxima de um ponto de ônibus. O ônibus chega, aguarda a chegada do caracol, abre a porta e espera enquanto o caracol sinaliza movimentando as antenas. Depois, a porta fecha e o ônibus parte.

A interação é coordenada por etapas: o ônibus só abre a porta depois que os dois personagens chegam e só parte depois de concluir o fechamento.

## Arquivos

- `main.py`: construção da cena 3D, modelos, câmera, iluminação, materiais e renderização.
- `animacao.py`: posições e etapas da animação controladas pelo tempo decorrido.
- `assets/asfalto.png`: textura de imagem aplicada ao chão.
- `requirements.txt`: dependências Python.
- `py3d/`: componentes do framework e shaders usados na aplicação, incluídos nesta pasta do projeto.
- `instalar_framework.py`: instala a pasta `py3d` quando ela ainda não estiver disponível.
- `tests/`: testes automatizados da animação e do instalador.
- `GUIA_CODIGO.md`: explicação dos principais trechos para estudo.
- `ROTEIRO_APRESENTACAO.md`: roteiro de demonstração.

## Instalação no Windows

Requer Python 3.11 e conexão com a internet na primeira instalação.

1. Baixe o repositório do portfólio pelo GitHub (**Code > Download ZIP**) ou clone o portfólio.
2. Entre na pasta `projetos/computacao-grafica-caracol-onibus`.
3. Execute `INICIAR.bat`.

O BAT cria um ambiente virtual, instala as dependências, prepara o framework Py3D e inicia a cena. Caso uma etapa falhe, ele interrompe a execução e mostra a mensagem correspondente.

Para rodar os testes, execute `TESTAR.bat` depois da instalação.

## Controles

- W/S: frente e trás.
- A/D: esquerda e direita.
- R/F: subir e descer.
- Q/E: girar a câmera.
- T/G: olhar para cima e para baixo.
- Espaço: pausar ou retomar a animação.

## Requisitos gráficos destacados

- Modelos compostos por caixas, esferas, elipsoides e cilindros.
- Translação, rotação, escala e hierarquia de objetos.
- Câmera em perspectiva controlada pelo teclado.
- Textura de imagem com coordenadas UV.
- Luz ambiente e luz direcional, materiais Phong e vetores normais.
- Shadow mapping por passagem de profundidade do framework.
- Animação baseada em delta time, com pausa e retomada.

## Fontes

- STEMKOSKI, Lee; PASCALE, Michael. *Developing Graphics Frameworks with Python and OpenGL*. CRC Press, 2022. DOI: https://doi.org/10.1201/9781003181378.
- Repositório público de exemplos associado ao livro: https://github.com/ax-va/PyOpenGL-Pygame-Stemkoski-Pascale-2021 (revisão `f3029550425385f90e0d66ba7f73bb310112039b`).

O projeto foi desenvolvido com apoio de IA na estruturação, comentários, testes e documentação. Os integrantes devem executar e compreender o código antes da apresentação.
