from typing import List


class BinarySearch:

    def find_index(self, value: int, values: List[int]) -> int:
        return self.find_in_subarray(value, values, 0, len(values) - 1)

    def find_in_subarray(self, value: int, values: List[int], min_index: int, max_index: int) -> int:
        if min_index <= max_index:
            midpoint = (max_index + min_index) // 2
            if value == values[midpoint]:
                return midpoint
            elif value > values[midpoint]:
                return self.find_in_subarray(value, values, midpoint + 1, max_index)
            else:
                return self.find_in_subarray(value, values, min_index, midpoint - 1)

        return -1  # indicates that the value was not found in the array


def main():
    my_values = [2, 4, 6, 8, 10]
    search = BinarySearch()
    for value in range(12):
        print(f'value: {value} Found at index: {search.find_index(value, my_values)}')


if __name__ == '__main__':
    main()