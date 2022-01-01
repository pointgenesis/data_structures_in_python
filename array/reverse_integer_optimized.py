
class ReverseInteger:

    def __init__(self) -> None:
        pass

    def reverse_integer(self, int_value) -> int:

        new_integer = int_value
        new_integer_value = 0
        iteration = 0
        while new_integer > 0:
            new_integer_slice = new_integer % 10
            new_integer = new_integer//10
            new_integer_value = (10 * iteration) + new_integer
            print(f'new_integer: {new_integer}')
            print(f'new_integer_value: {new_integer_value}')
        return 0


if __name__ == '__main__':
    integer_value = 1234
    reverse_integer = ReverseInteger()
    reversed_integer_value = reverse_integer.reverse_integer(integer_value)
    print(f'reversed_integer_value: {reversed_integer_value}')

    print(4321 % 10)
    print(4321//10)
