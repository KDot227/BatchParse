from BatchParse import parse_heavy

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
echo hello world && echo this is a test

pause
exit"""

parsed = parse_heavy(code, parse_and=True)
print(parsed)
