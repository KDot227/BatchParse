def parse(code: str, parse_and: bool = False) -> list:
    """Parse initial Batch Code

    Args:
        code (str): Inital Batch Code to Parse

    Returns:
        list: Returns Parsed Batch Code as an Array
    """
    code_to_array = code.split("\n")

    if parse_and:
        code_to_array = __parse_and(code_to_array)

    parsed_code = []

    allowed_methods = ["@"]

    ignorable_lines = ["\n", ""]

    # if line doesn't start with a letter then we just ignore everything up until the first letter

    # remove all lines that start with ignorable_lines
    for line in code_to_array:
        if line in ignorable_lines:
            code_to_array.remove(line)

    for line in code_to_array:
        if not line[0].isalpha() and not line[0] in allowed_methods:
            for char in line:
                if char.isalpha():
                    parsed_code.append(line[line.index(char) :])
                    break
        else:
            parsed_code.append(line)

    return parsed_code


def parse_heavy(code: str, parse_and: bool = False) -> list:
    """Parses code and returns a dict with all the elements of the code and different infot that the user might want to know

    Args:
        code (str): Code to Parse
        parse_and (bool, optional): if user wants to parse and Defaults to False.

    Returns:
        list: Parsed code as a list with [[code, dict], [code, dict], [code, dict]] (EXAMPLE)
    """

    final_arr = []

    initial_parse = parse(code, parse_and)
    for array in initial_parse:
        dict_parse = info_gather(array)
        final_arr.append([array, dict_parse])

    return final_arr


def get_method(line: str) -> str:
    """Get's the Method from a line of Batch Code

    Args:
        line (str): Line of Batch Code

    Returns:
        str: Returns the Method of the Batch Code
    """
    return line.split(" ")[0]


def get_args(line: str) -> str:
    """Get's the Arguments from a line of Batch Code

    Args:
        line (str): Line of Batch Code

    Returns:
        str: Returns the Arguments of the Batch Code as a single string
    """
    return " ".join(line.split(" ")[1:])


def __parse_and(code: list) -> list:
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


def info_gather(code: str) -> dict:
    """Gathers information about the code

    Args:
        code (str): Code to gather information about

    Returns:
        dict: Returns a dict with the information about the code
    """
    info = {"method": get_method(code), "args": get_args(code), "raw": code}

    return info
