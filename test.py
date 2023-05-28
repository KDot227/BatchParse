from BatchParse import parse

code = """
@echo off
echo this is a test
echo this is a test
echo this is a test

pause
exit
"""

parsed = parse(code)
print(parsed)
