@echo off
REM Pastebin Setup Script for Windows

echo === Pastebin-Lite Setup ===
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3.11+
    exit /b 1
)
echo [OK] Python found

REM Check Node
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js not found. Please install Node.js 18+
    exit /b 1
)
echo [OK] Node.js found

echo.
echo Installing backend dependencies...
cd bakendpastebin
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install Python dependencies
    exit /b 1
)

echo.
echo Running Django migrations...
python manage.py migrate
if errorlevel 1 (
    echo ERROR: Failed to run migrations
    exit /b 1
)

cd ..

echo.
echo Installing frontend dependencies...
cd pastebin
call npm install
if errorlevel 1 (
    echo ERROR: Failed to install npm dependencies
    exit /b 1
)

cd ..

echo.
echo =================================
echo [SUCCESS] Setup Complete!
echo =================================
echo.
echo To start the application:
echo.
echo Terminal 1 (Backend):
echo   cd bakendpastebin
echo   python manage.py runserver
echo.
echo Terminal 2 (Frontend):
echo   cd pastebin
echo   npm start
echo.
echo Then visit: http://localhost:3000
echo.
pause
