from typing import List


def visit(value: str, index: int = 0, char_array: List[str] = None) -> List[str]:
    """ This function is for demonstration purposes only. By default strings are referencable using indexes. """
    if char_array is None:
        char_array = []

    if index < len(value):
        char_array.append(value[index])
        return visit(value, index + 1, char_array)

    return char_array


print(visit("hello"))
