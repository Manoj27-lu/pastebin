#!/bin/bash

# Pastebin Setup and Test Script
# Run this to verify everything is working

echo "=== Pastebin-Lite Setup Verification ==="
echo ""

# Check Python
echo "✓ Checking Python..."
python --version || { echo "✗ Python not installed"; exit 1; }

# Check Node
echo "✓ Checking Node.js..."
node --version || { echo "✗ Node.js not installed"; exit 1; }

# Check pip
echo "✓ Checking pip..."
pip --version || { echo "✗ pip not installed"; exit 1; }

# Check npm
echo "✓ Checking npm..."
npm --version || { echo "✗ npm not installed"; exit 1; }

echo ""
echo "=== Installing Backend Dependencies ==="
cd bakendpastebin
pip install -r requirements.txt

echo ""
echo "=== Running Django Migrations ==="
python manage.py migrate

echo ""
echo "=== Installing Frontend Dependencies ==="
cd ../pastebin
npm install

echo ""
echo "✅ Setup Complete!"
echo ""
echo "To run the application:"
echo ""
echo "Terminal 1 (Backend):"
echo "  cd bakendpastebin"
echo "  python manage.py runserver"
echo ""
echo "Terminal 2 (Frontend):"
echo "  cd pastebin"
echo "  npm start"
echo ""
echo "Then visit: http://localhost:3000"
