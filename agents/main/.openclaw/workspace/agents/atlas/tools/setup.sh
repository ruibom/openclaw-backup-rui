#!/bin/bash
# Setup script for LinkedIn Analytics tool
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"

echo "Setting up LinkedIn Analytics tool..."

# Create virtual environment
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
fi

# Activate and install
source "$VENV_DIR/bin/activate"
pip install playwright
playwright install chromium

echo "Setup complete. Virtual env at: $VENV_DIR"
echo "Usage: source $VENV_DIR/bin/activate && python $SCRIPT_DIR/linkedin_analytics.py <post_url>"