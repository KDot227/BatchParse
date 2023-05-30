def get_method(line: str) -> str:
    """Get's the Method from a line of Batch Code

    Args:
        line (str): Line of Batch Code

    Returns:
        str: Returns the Method of the Batch Code
    """
    out = line.split(" ")[0]
    if not out.startswith(":"):
        return out
    else:
        return "label: " + out[1:]


def get_args(line: str) -> str:
    """Get's the Arguments from a line of Batch Code

    Args:
        line (str): Line of Batch Code

    Returns:
        str: Returns the Arguments of the Batch Code as a single string
    """
    return " ".join(line.split(" ")[1:])


def info_gather(code: str) -> dict:
    """Gathers information about the code

    Args:
        code (str): Code to gather information about

    Returns:
        dict: Returns a dict with the information about the code
    """
    info = {
        "method": get_method(code),
        "args": get_args(code),
        "length": __get_length(code),
        "valid_command_length": valid_length(__get_length(code)),
        "echo_to_file": echo_to_file(code),
        "get_from_file": get_from_file(code),
        "raw": code,
    }

    return info


def __get_length(code: str) -> int:
    """Get's the length of the code

    Args:
        code (str): Code to get the length of

    Returns:
        int: Returns the length of the code
    """

    # NOTE THIS MIGHT NOT BE ACCURATE DUE TO CODEPAGES AND OTHER FACTORS!!!
    return len(code)


def valid_length(length: int) -> bool:
    """Check if the length of the code is valid with windows batch standards or else the command overflows

    Args:
        length (int): Initial Length of command

    Returns:
        bool: True or False if the length is valid
    """
    return length <= 8191


def echo_to_file(code: str) -> bool:
    possible_methods = [">", ">>"]
    unallowed_methods = ["^>", "^>>", ">^>", "^>^>"]
    return any([method in code for method in possible_methods]) and not any(
        [method in code for method in unallowed_methods]
    )


def get_from_file(code: str) -> bool:
    possible_methods = ["<"]
    unallowed_methods = ["^<"]
    return any([method in code for method in possible_methods]) and not any(
        [method in code for method in unallowed_methods]
    )
