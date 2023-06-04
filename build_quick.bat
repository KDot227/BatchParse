@echo off

cd /d %~dp0

pip install .

python %~dp0\test\test.py