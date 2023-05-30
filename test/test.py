from BatchParse import parse_heavy

from rich import print

# code = """
# @echo off
# echo this is a test
# echo this is a test
# echo this is a test
#
# pause
# exit
# """

code = """
@echo off
echo hello world && echo this is a test ^
pause
if 1==1 (
    echo hello world
    echo this is a test
)
exit"""

parsed = parse_heavy(code)
print(parsed)
