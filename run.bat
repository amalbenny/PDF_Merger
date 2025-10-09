@echo off
cd /d %~dp0

REM Create virtual environment if it doesn't exist
if not exist .venv\Scripts\activate.bat (
    python -m venv .venv
)

call .venv\Scripts\activate
python __main__.py
