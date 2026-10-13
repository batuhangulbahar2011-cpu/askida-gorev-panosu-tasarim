@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Python ortamı bulunamadı. ANA-SITE.md dosyasındaki kurulum adımlarını izleyin.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" manage.py migrate --noinput
if errorlevel 1 goto hata
".venv\Scripts\python.exe" manage.py kurulum
if errorlevel 1 goto hata
echo.
echo Ana site: http://127.0.0.1:8000/
echo Bu pencere açık kaldığı sürece site çalışır. Durdurmak için Ctrl+C.
".venv\Scripts\python.exe" manage.py runserver 127.0.0.1:8000 --noreload
if errorlevel 1 goto hata
exit /b 0
:hata
echo İşlem tamamlanamadı. Yukarıdaki hata mesajını paylaşın.
pause
exit /b 1
