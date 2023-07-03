@echo off
cd ManagerProject
start main.exe
mode con cols=80 lines=3000
timeout /T 2 /NOBREAK > nul

cd ..

set /p task_number=<ManagerCounter.txt
set task_folder_name=Task%task_number%

echo The number is %task_number%
cd %task_folder_name%
code .

exit