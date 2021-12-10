
class MoveZerosLeft:

    def __init__(self):
        pass
    # end init

    def inspect(self, array_of_numbers):
        print(f"array_of_numbers: {array_of_numbers}")

        head_index = 0
        current_index = 0
        for number in array_of_numbers:
            print(f"number: {number}")
            if 0 == number:
                print(f'number: {number} head_index: {head_index} current_index: {current_index}')
                self.shift_and_insert(number, head_index, current_index, array_of_numbers)
                head_index += 1
            # end if
            current_index += 1
        # end for
    # end inspect

    def shift_and_insert(self, number, head_index, current_index, numbers):
        print(f'head_index: {head_index} current_index: {current_index} numbers: {numbers}')
        idx = current_index
        while head_index <= idx <= current_index:
            numbers[idx] = numbers[idx-1]
            idx -= 1
        # end while
        numbers[head_index] = number
        print(f'numbers: {numbers}')
    # end shift_and_insert


if __name__ == "__main__":
    move_zeros_left = MoveZerosLeft()
    move_zeros_left.inspect([3, 2, 9, 0, 5, 8, 6, 0, 1, 0])
# end if

# end class
