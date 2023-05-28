@echo off

python -m pip uninstall BatchParse -y
python -m setup.py bdist_wheel

for /F "delims=" %%i in ('dir /b dist\*.whl') do set "whl=%%i"

python -m pip install dist\%whl%