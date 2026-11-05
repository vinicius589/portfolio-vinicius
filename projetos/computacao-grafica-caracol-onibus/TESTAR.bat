@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Ambiente virtual nao encontrado.
    echo Execute INICIAR.bat primeiro para instalar as dependencias.
    goto FALHA
)

call ".venv\Scripts\activate.bat"
if errorlevel 1 goto FALHA

python -m pytest -q
if errorlevel 1 goto FALHA

echo.
echo Todos os testes foram executados com sucesso.
goto FIM

:FALHA
echo.
echo Nao foi possivel executar os testes.
pause
exit /b 1

:FIM
pause
endlocal
