# Guia para entender o codigo

Este guia acompanha o codigo-fonte. A ideia e entender primeiro a funcao de cada arquivo e depois seguir a ordem da animacao.

## 1. Arquivos principais

- `main.py`: monta a janela, a cena, os personagens, a camera, a iluminacao e chama a renderizacao.
- `animacao.py`: controla as posicoes e a sequencia de acoes.
- `py3d/`: framework usado para geometrias, materiais, camera, luzes, shaders e shadow mapping.
- `assets/asfalto.png`: imagem usada como textura do chao.
- `instalar_framework.py`: baixa o framework apenas quando ele ainda nao esta instalado.

## 2. Como a animacao funciona

A classe `SequenciaAnimacao` guarda as informacoes da cena. As variaveis mais importantes sao:

- `x_caracol`: posicao horizontal do caracol.
- `z_onibus`: posicao do onibus no percurso.
- `porta`: valor entre 0 e 1; 0 significa fechada e 1 significa aberta.
- `etapa`: informa em qual parte da sequencia estamos.
- `tempo_etapa`: conta quanto tempo passou na etapa atual.

O metodo `atualizar(delta_tempo)` recebe o tempo decorrido desde o quadro anterior. Por isso, a velocidade da animacao depende do tempo e nao diretamente da quantidade de quadros por segundo.

A sequencia e:

1. aproximacao: caracol e onibus se deslocam;
2. abrir: a porta abre aos poucos;
3. sinalizar: o caracol balanca as antenas e o onibus espera;
4. fechar: a porta fecha;
5. partir: o onibus retoma o percurso;
6. espera: pequena pausa antes de repetir.

O metodo `onibus_esta_se_movendo()` informa quando as rodas devem girar. Assim, elas param quando o onibus espera.

## 3. Como a cena 3D e montada

No arquivo `main.py`:

- `initialize()`: prepara a cena e cria os materiais, luzes, camera e objetos.
- `criar_ambiente()`: cria o chao, a calcada, a faixa e o ponto.
- `criar_onibus()`: monta a carroceria, janelas, rodas, farois e porta.
- `criar_caracol()`: monta corpo, casco, sensor e antenas.
- `criar_antena()`: cria uma antena como um grupo separado para poder gira-la.
- `adicionar_peca()`: cria uma malha, posiciona e a adiciona a um grupo.
- `criar_material()`: prepara materiais com iluminacao Phong.
- `update()`: atualiza a animacao e desenha cada quadro.

## 4. Transformacoes e hierarquia

- Translacao muda a posicao: `set_position()`.
- Rotacao muda a orientacao: `rotate_x()`, `rotate_y()` e `rotate_z()`.
- Escala muda o tamanho: `scale()`.

O onibus e o caracol sao grupos. As partes ficam dentro desses grupos. Quando o grupo se move, todas as pecas acompanham. As antenas tambem sao grupos separados, permitindo mover o caracol sem perder o movimento articulado.

## 5. Camera, pausa e controles

A camera usa projecao em perspectiva. O `MovementRig` recebe as teclas e movimenta a camera. A tecla Espaco altera a variavel `pausado`. A camera continua funcionando durante a pausa, mas a sequencia dos personagens fica parada.

## 6. Textura, iluminacao e sombras

A textura `assets/asfalto.png` e carregada pela classe `Texture` e aplicada ao chao. As geometrias fornecem coordenadas UV, usadas para localizar os pontos da imagem na superficie.

A cena usa uma luz ambiente e uma luz direcional. Os materiais Phong usam as normais dos vertices para calcular como a luz atinge cada superficie.

O shadow mapping e diferente do calculo de iluminacao. O renderer primeiro faz uma passagem pela camera da luz e grava a profundidade dos objetos na textura de sombra. Depois, no desenho normal, o shader Phong compara a profundidade do ponto com a que foi gravada. Quando um objeto esta entre a luz e a superficie, essa regiao fica escurecida.

Os shaders utilizados estao em:

- `py3d/material/phong.py`: vertex shader e fragment shader da iluminacao Phong e leitura da sombra;
- `py3d/material/depth.py`: shader usado na passagem de profundidade;
- `py3d/core_ext/renderer.py`: organiza as duas passagens de renderizacao;
- `py3d/light/shadow.py`: configura camera, textura, intensidade e bias da sombra.

## 7. Perguntas que podem aparecer

**O que e delta time?**
E o tempo decorrido desde o quadro anterior. Ele permite calcular deslocamentos por segundo.

**Qual a diferenca entre sombreamento e sombra projetada?**
Sombreamento calcula a aparencia da superficie conforme luz e normais. Sombra projetada e a regiao bloqueada por outro objeto, calculada pelo mapa de profundidade.

**Por que usar grupos?**
Para organizar as partes e aplicar uma transformacao ao conjunto sem ter de mover cada peca separadamente.

**Como a interacao e garantida?**
O onibus espera os dois personagens chegarem. Depois abre a porta, aguarda o sinal do caracol, fecha a porta e so entao parte.

Estude principalmente `animacao.py` e o metodo `update()`, pois eles mostram a logica mais importante da apresentacao.
