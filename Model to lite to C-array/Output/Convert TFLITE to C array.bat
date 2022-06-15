@echo off
echo This batch script uses the windows subsystem for linux
echo if this is not installed the script will fail
echo please type in the filename without extention
echo to exit this script type "exit"
:start
set /p FILENAME="File to convert: "
if %FILENAME% == exit exit
:convert
echo The file you picked is %FILENAME%
echo converting
wsl.exe xxd -i %FILENAME%.tflite > %FILENAME%.cc
echo converting complete
goto start

