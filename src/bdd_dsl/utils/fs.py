import re


def get_valid_filename(name):
    """
    based on same function from https://github.com/django/django/blob/main/django/utils/text.py
    also convert ':' to '__' and '/' to '_'

    Return the given string converted to a string that can be used for a clean
    filename. Remove leading and trailing spaces; convert other spaces to
    underscores; and remove anything that is not an alphanumeric, dash,
    underscore, or dot.
    >>> get_valid_filename("john's portrait in 2004.jpg")
    'johns_portrait_in_2004.jpg'
    """
    s = str(name).strip().replace(" ", "_")
    s = str(s).strip().replace(":", "__")
    s = str(s).strip().replace("/", "_")
    s = re.sub(r"(?u)[^-\w.]", "", s)
    if s in {"", ".", ".."}:
        # suspicious file name
        raise ValueError(f"Could not derive file name from '{name}'")
    return s
