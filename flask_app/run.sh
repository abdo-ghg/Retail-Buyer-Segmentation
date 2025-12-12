#!/bin/bash

echo "============================================"
echo "  Retail Buyer Segmentation - Flask App"
echo "============================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Install/upgrade dependencies
echo "Installing dependencies..."
pip install -r requirements.txt --quiet
echo ""

# Create necessary directories
mkdir -p uploads
mkdir -p static/images
echo "Directories created/verified."
echo ""

# Run the Flask application
echo "============================================"
echo "  Starting Flask Application..."
echo "  Access at: http://localhost:5000"
echo "============================================"
echo ""
python app.py
