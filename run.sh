#!/bin/bash
cd "$(dirname "$0")"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
	python3 -m venv .venv
fi

source .venv/bin/activate
python3 __main__.py
