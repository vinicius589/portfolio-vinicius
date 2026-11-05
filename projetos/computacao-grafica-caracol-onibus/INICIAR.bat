@echo off
setlocal
cd /d "%~dp0"

rem Confere se o Python 3.11 esta instalado antes de criar o ambiente.
py -3.11 --version >nul 2>&1
if errorlevel 1 goto PYTHON_NAO_ENCONTRADO

rem Cria um ambiente virtual isolado para este projeto.
if not exist ".venv\Scripts\python.exe" (
    echo Criando o ambiente virtual...
    py -3.11 -m venv .venv
    if errorlevel 1 goto ERRO_AMBIENTE
)

rem Ativa o ambiente e instala as bibliotecas do projeto.
call ".venv\Scripts\activate.bat"
if errorlevel 1 goto ERRO_ATIVACAO

echo.
echo Instalando as bibliotecas do projeto...
python -m pip install -r requirements.txt
if errorlevel 1 goto ERRO_BIBLIOTECAS

rem Baixa o framework do livro. O script informa claramente se houver falha.
echo.
echo Preparando o framework Py3D...
python instalar_framework.py
if errorlevel 1 goto ERRO_FRAMEWORK

rem Inicia a aplicacao grafica.
echo.
echo Iniciando o trabalho de Computacao Grafica...
python main.py
if errorlevel 1 goto ERRO_EXECUCAO

goto FIM

:PYTHON_NAO_ENCONTRADO
echo.
echo ERRO: Python 3.11 nao foi encontrado.
echo Instale o Python 3.11 e marque a opcao "Add Python to PATH".
echo Depois abra este arquivo novamente.
goto FALHA

:ERRO_AMBIENTE
echo.
echo ERRO: nao foi possivel criar o ambiente virtual.
goto FALHA

:ERRO_ATIVACAO
echo.
echo ERRO: nao foi possivel ativar o ambiente virtual.
goto FALHA

:ERRO_BIBLIOTECAS
echo.
echo ERRO: falha ao instalar as bibliotecas.
echo Confira a conexao com a internet e a versao do Python.
goto FALHA

:ERRO_FRAMEWORK
echo.
echo ERRO: nao foi possivel instalar o framework Py3D.
echo Confira a conexao com a internet e tente novamente.
goto FALHA

:ERRO_EXECUCAO
echo.
echo ERRO: a aplicacao foi encerrada com falha.
echo Confira a mensagem exibida acima.
goto FALHA

:FALHA
echo.
pause
exit /b 1

:FIM
endlocal
