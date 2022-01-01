class ReverseArray:

    def __init__(self):
        pass

    def reverse(self, array) -> None:
        length = len(array)

        for left_index in range(length//2):
            right_index = (length - 1) - left_index
            array[left_index], array[right_index] = array[right_index], array[left_index]


if __name__ == '__main__':
    sorted_array = [1, 0, 4]
    reverse_array = ReverseArray()
    reverse_array.reverse(sorted_array)
    print(sorted_array)