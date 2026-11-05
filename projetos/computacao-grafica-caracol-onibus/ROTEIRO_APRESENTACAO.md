# Roteiro de apresentacao - Computacao Grafica

## 1. Apresentacao da ideia

Nosso projeto representa um ponto de onibus. Um caracol robotico se aproxima do ponto e interage com um onibus de brinquedo. A ideia e mostrar dois objetos diferentes realizando uma acao coordenada.

## 2. Demonstracao da cena

Mostre o caracol e o onibus na tela. Explique que os modelos foram montados com formas geometricas do framework: caixas, esferas, cilindros e elipsoides.

Deixe a animacao acontecer:

1. o caracol se aproxima;
2. o onibus chega e aguarda;
3. a porta abre;
4. o caracol movimenta as antenas;
5. a porta fecha;
6. o onibus parte.

Explique que o onibus nao parte enquanto a porta nao termina de fechar.

## 3. Mostrar os controles

Use W, A, S, D, R e F para movimentar a camera, Q e E para girar e T e G para olhar para cima e para baixo. Pressione Espaco para pausar e retomar a animacao.

## 4. Explicar o codigo

Comece por `animacao.py`. Mostre a classe `SequenciaAnimacao`, as variaveis de posicao, a variavel `etapa` e o metodo `atualizar(delta_tempo)`.

Depois abra `main.py`. Explique que `initialize()` prepara a cena, `criar_onibus()` e `criar_caracol()` montam os modelos, e `update()` atualiza os personagens e chama o renderer.

## 5. Conceitos graficos

- Transladar e mudar a posicao.
- Rotacionar e mudar a orientacao.
- Escalar e mudar o tamanho.
- A hierarquia organiza as pecas em grupos.
- A camera em perspectiva e controlada pelo teclado.
- A textura do asfalto usa coordenadas UV.
- A iluminacao Phong calcula o efeito da luz sobre as superficies.
- O shadow mapping grava a profundidade vista pela luz e usa essa informacao para desenhar a sombra projetada.

## 6. Divisao da apresentacao

Cada integrante deve explicar sua contribuicao real e demonstrar que conhece a aplicacao completa. Preencham a divisao somente depois de combinar quem fez cada parte.

## 7. Antes de apresentar

- Confirmar que os dois temas foram sorteados ou autorizados pelo professor.
- Executar a aplicacao no computador da apresentacao.
- Testar os controles, a pausa, a textura, a iluminacao e a sombra.
- Saber explicar a diferenca entre sombrear uma superficie e projetar uma sombra.
- Informar os nomes dos integrantes e suas contribuicoes reais.
