import re
from typing import List, Union


def parse_and(code: list) -> list:
    """
    Parse the Batch Code for the AND Operator

    Args:
        code (list): Batch Code as an Array

    Returns:
        list: Returns Parsed Batch Code as an Array
    """
    parsed_code = []

    for line in code:
        if " & " in line or " && " in line:
            if " & " in line:
                parsed_code.extend(line.split(" & "))
            elif " && " in line:
                parsed_code.extend(line.split(" && "))
        else:
            parsed_code.append(line)

    return parsed_code


def parse_carrot(code: list) -> list:
    """Parses the Batch Code for the Carrot Operator

    Args:
        code (list): Batch Code as an Array

    Returns:
        list: Returns Parsed Batch Code as an Array
    """
    # if the line ends with a carrot then it's escaping the next line character so we add that line to the old one as if there was just a space
    for line in code:
        if line.endswith("^"):
            index = code.index(line)
            code[index] = code[index] + " " + code[index + 1]
            code.pop(index + 1)

    return code


def parse_script_block(
    code: Union[List[str], str], ignore_indents: bool = False
) -> list:
    """Parses the Batch Code for Script Blocks

    Args:
        code (list): Batch Code as an Array

    Returns:
        list: Returns Parsed Batch Code as an Array
    """

    if isinstance(code, list):
        code = "".join(code)

    if ignore_indents:
        for line in code:
            ammount_of_indents = len(re.findall("^ *", line)[0])
            if ammount_of_indents >= 12:
                raise Exception(
                    "You have more than 12 spaces for 1 indent. Please don't use more than 4 and chain your indents into 1 line."
                )

    parsed_code = []
    i = 0
    while i < len(code):
        line = code[i].strip()

        if line.endswith("("):
            while not line.endswith(")"):
                i += 1
                next_line = code[i].strip()
                # Add '&' between lines cause it can't just do stuff like allat
                line += " & " + next_line

            line = line.replace("\n", " ").replace("\r", "")
            line = " ".join(line.split())

            # regex cause im a RE tard
            # that was funny asf ngl
            matches = re.findall(r"\((.*?)\)", line)
            for match in matches:
                if match.startswith(" &"):
                    modified_match = match[2:-2]
                    line = line.replace(match, modified_match)
                else:
                    modified_match = match

        if line:
            parsed_code.append(line + "\n")
        i += 1
    return parsed_code
