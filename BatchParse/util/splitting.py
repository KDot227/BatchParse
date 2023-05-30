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
