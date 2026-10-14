@echo off
cd /d "%~dp0"
echo ==========================================
echo   Push Prompt Injection Shield to GitHub
echo ==========================================
echo.

where git >nul 2>&1
if errorlevel 1 (
  echo Git is not installed. Download it from https://git-scm.com and install with default options, then run this file again.
  pause
  exit /b
)

if not exist app.py (
  echo app.py not found here. Save this file in the SAME folder as app.py and run it again.
  pause
  exit /b
)

set /p GHNAME=Enter your full name: 
set /p GHEMAIL=Enter your GitHub email: 
set /p GHUSER=Enter your GitHub username: 

git config --global user.name "%GHNAME%"
git config --global user.email "%GHEMAIL%"
git init
git add .

echo.
echo ===== FILES THAT WILL BE UPLOADED =====
git status
echo.
echo CHECK THE LIST ABOVE: "venv" and any ".zip" file must NOT appear.
echo.
set /p OK=Type Y and press Enter to continue, or anything else to stop: 
if /i not "%OK%"=="Y" (
  echo Stopped. Nothing was uploaded.
  pause
  exit /b
)

git commit -m "Prompt injection shield"
git branch -M main
git remote remove origin >nul 2>&1
git remote add origin https://github.com/%GHUSER%/prompt-injection-shield.git
git push -u origin main

echo.
echo Done. Refresh your GitHub repo page to see your files.
pause
