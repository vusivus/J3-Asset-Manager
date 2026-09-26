@echo off
cd /d "%~dp0"
java -jar "J3 Asset Manager.jar"
if errorlevel 1 (
    echo.
    echo J3 Asset Manager could not start. The error is shown above.
    pause
)
