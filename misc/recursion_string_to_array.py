from typing import List


def visit(value: str, index: int = 0, new_value: List[str] = None) -> List[str]:
    """ This function is for demonstration purposes only. By default strings are referencable using indexes. """
    if new_value is None:
        new_value = []

    if index < len(value):
        new_value.append(value[index])
        return visit(value, index + 1, new_value)

    return new_value


print(visit("hello"))
