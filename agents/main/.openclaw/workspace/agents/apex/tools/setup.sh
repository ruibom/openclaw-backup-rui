#!/bin/bash
# Setup LinkedIn Analytics for Apex
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"

echo "Setting up LinkedIn Analytics..."

if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"
pip install playwright
playwright install chromium

echo "✓ Setup complete. Usage:"
echo "  source $VENV_DIR/bin/activate"
echo "  python $SCRIPT_DIR/linkedin_analytics.py <post_url>"
