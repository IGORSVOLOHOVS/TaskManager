@echo off
setlocal

:: Получаем текущую дату и время
for /f "tokens=2 delims==" %%a in ('"wmic os get localdatetime /value"') do set "datetime=%%a"
set "datestamp=%datetime:~0,8%"
set "timestamp=%datetime:~8,6%"

:: Установка путей
set "repoURL=https://github.com/IGORSVOLOHOVS/TaskManager.git"
set "cloneDir=%temp%\%datestamp%-%timestamp%"
set "targetDir=C:\Users\User\Projects\Task-%datestamp%-%timestamp%"

:: Клонирование репозитория
git clone "%repoURL%" "%cloneDir%"

:: Копирование папки TaskTools в целевую директорию
xcopy /E /I "%cloneDir%\TaskTools" "%targetDir%"

:: Открытие целевой директории в VS Code
code "%targetDir%"

:: Удаление временной папки с клоном репозитория
rd /s /q "%cloneDir%"

endlocal
