@echo off
cd /d %~dp0

REM Create virtual environment if it doesn't exist
if not exist .venv\Scripts\activate.bat (
    python -m venv .venv
    call .venv\Scripts\activate
    if errorlevel 1 (
        echo Failed to activate virtual environment
        exit /b 1
    )
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo Failed to install requirements
        exit /b 1
    )
) else (
    call .venv\Scripts\activate
    if errorlevel 1 (
        echo Failed to activate virtual environment
        exit /b 1
    )
)

python __main__.py
pause
