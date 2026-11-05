# Resultado dos testes automatizados

Data da revisao: 04/11/2026.

## Testes executados no ambiente de desenvolvimento

- Sintaxe Python: compilacao de `main.py`, `animacao.py`, `instalar_framework.py` e dos testes concluida sem erro.
- Testes automatizados: **12 aprovados**.
- Testes da sequencia: chegada conjunta, abertura, sinalizacao, fechamento, partida, reinicio, delta time e rodas paradas durante a espera.
- Testes do instalador: framework ja valido, extracao seletiva de ZIP e rejeicao de ZIP sem a pasta esperada.

## Limitacao desta validacao

A janela 3D ainda precisa ser executada em um Windows com Python 3.11 e driver OpenGL. O ambiente usado nesta revisao tem Python 3.13 e nao possui Pygame nem PyOpenGL instalados, portanto nao foi possivel comprovar a renderizacao visual nesta etapa.

## Como repetir

No Windows, execute `INICIAR.bat`. Depois, execute `TESTAR.bat` para repetir os 12 testes.
