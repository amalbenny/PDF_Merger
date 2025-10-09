@echo off
cd /d %~dp0

REM Create virtual environment if it doesn't exist
if not exist .venv\Scripts\activate.bat (
    python -m venv .venv
    call .venv\Scripts\activate && pip install -r requirements.txt
    
) else (
    call .venv\Scripts\activate
)
REM Run the main Python script In Environment
python __main__.py
pause
