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

code = """@echo off

for %%I in (1,2,3,4,5,6,7,8,9,10) do echo %%I"""

code = code.split("\n")

parsed = parse_heavy(code)
print(parsed)
