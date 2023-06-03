import logging

from .util.info import *
from .util.splitting import *
from .util.settings import Settings

from rich.logging import RichHandler
from rich.traceback import install

install(show_locals=True)

debug = False

handler = RichHandler(rich_tracebacks=True, tracebacks_show_locals=True)

if debug:
    logging.basicConfig(
        level=logging.DEBUG, format="%(message)s", datefmt="[%X]", handlers=[handler]
    )
else:
    logging.basicConfig(
        level=logging.INFO, format="%(message)s", datefmt="[%X]", handlers=[handler]
    )
logger = logging.getLogger("rich")


def parse(
    code,
    bsplit_and: bool = True,
    bsplit_carrot: bool = True,
    bsplit_script_block: bool = True,
) -> list:
    """Parse initial Batch Code

    Args:
        code (str): Inital Batch Code to Parse

    Returns:
        list: Returns Parsed Batch Code as an Array
    """

    if isinstance(code, str):
        code_to_array = code.split("\n")
    elif isinstance(code, list):
        code_to_array = code
    else:
        raise TypeError("code must be a string or list")

    functions = [
        parse_and,
        parse_carrot,
        # parse_script_block,
    ]

    bool_parse = [
        bsplit_and,
        bsplit_carrot,
        # bsplit_script_block,
    ]

    for function in functions:
        if bool_parse[functions.index(function)]:
            code_to_array = function(code_to_array)

    parsed_code = []

    allowed_methods = Settings.allowed_methods

    ignorable_lines = Settings.ignorable_lines

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


def parse_heavy(code: str, bsplit_and: bool = True) -> list:
    """Parses code and returns a dict with all the elements of the code and different infot that the user might want to know

    Args:
        code (str): Code to Parse
        parse_and (bool, optional): if user wants to parse and Defaults to False.
    Returns:
        list: Parsed code as a list with [[code, dict], [code, dict], [code, dict]] (EXAMPLE)
    """

    final_arr = []

    initial_parse = parse(code, bsplit_and=bsplit_and)
    logger.debug(f"Initial Parse: {initial_parse}")
    for array in initial_parse:
        logger.debug(f"Array: {array}")
        dict_parse = info_gather(array)
        logger.debug(f"Dict Parse: {dict_parse}")
        final_arr.append([array, dict_parse])

    return final_arr
