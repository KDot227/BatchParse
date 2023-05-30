import logging

from .util.info import *
from .util.splitting import *
from .util.settings import Settings

from rich.logging import RichHandler
from rich.progress import track
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


def parse(code: str, split_and: bool = False) -> list:
    """Parse initial Batch Code

    Args:
        code (str): Inital Batch Code to Parse

    Returns:
        list: Returns Parsed Batch Code as an Array
    """
    code_to_array = code.split("\n")

    if split_and:
        code_to_array = parse_and(code_to_array)

    parsed_code = []

    allowed_methods = Settings.allowed_methods

    ignorable_lines = Settings.ignorable_lines

    # if line doesn't start with a letter then we just ignore everything up until the first letter

    # remove all lines that start with ignorable_lines
    for line in code_to_array:
        if line in ignorable_lines:
            code_to_array.remove(line)

    for line in track(code_to_array, description="Parsing Batch Code LIGHT..."):
        if not line[0].isalpha() and not line[0] in allowed_methods:
            for char in line:
                if char.isalpha():
                    parsed_code.append(line[line.index(char) :])
                    break
        else:
            parsed_code.append(line)

    return parsed_code


def parse_heavy(code: str, split_and: bool = False) -> list:
    """Parses code and returns a dict with all the elements of the code and different infot that the user might want to know

    Args:
        code (str): Code to Parse
        parse_and (bool, optional): if user wants to parse and Defaults to False.
    Returns:
        list: Parsed code as a list with [[code, dict], [code, dict], [code, dict]] (EXAMPLE)
    """

    final_arr = []

    initial_parse = parse(code, split_and=split_and)
    logger.debug(f"Initial Parse: {initial_parse}")
    for array in track(initial_parse, description="Parsing Batch Code HEAVY..."):
        logger.debug(f"Array: {array}")
        dict_parse = info_gather(array)
        logger.debug(f"Dict Parse: {dict_parse}")
        final_arr.append([array, dict_parse])

    return final_arr
