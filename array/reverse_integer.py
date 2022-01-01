
class ReverseInteger:

    def __init__(self) -> None:
        pass

    def reverse_integer(self, int_value) -> int:
        str_values = list(str(int_value))
        length = len(str_values)
        for left_idx in range(length//2):
            right_idx = (length - 1) - left_idx
            str_values[left_idx], str_values[right_idx] = str_values[right_idx], str_values[left_idx]

        return int("".join(str_values))


if __name__ == '__main__':
    integer_value = 1234
    reverse_integer = ReverseInteger()
    reversed_integer_value = reverse_integer.reverse_integer(integer_value)
    print(f'reversed_integer_value: {reversed_integer_value}')
