#!/usr/bin/python3
"""function that prints a text with 2 new lines after each,of these characters: . ? and :
Attributes:
    text_indentation: function that prints a text
"""


def text_indentation(text):
    """Prints a text with 2 new lines after .?: characters.

    Args:
        text: string to be printed.

    Raises:
        TypeError: If text is not of type str.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
