#!/bin/bash
cd "$(dirname "$0")"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    python3 -m venv .venv || { echo "Failed to create virtual environment"; exit 1; }
    source .venv/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }
    python3 -m pip install -r requirements.txt || { echo "Failed to install requirements"; exit 1; }
else
    source .venv/bin/activate || { echo "Failed to activate virtual environment"; exit 1; }
fi

python3 __main__.py
