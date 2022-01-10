from typing import List


class BinarySearch:

    def search(self, numbers: List[int], lower_index: int, upper_index: int, value: int) -> int:
        if upper_index >= lower_index:
            midpoint = (upper_index + lower_index) // 2
            if numbers[midpoint] == value:
                return midpoint
            elif numbers[midpoint] > value:
                return self.search(numbers, lower_index, midpoint - 1, value)
            else:
                return self.search(numbers, midpoint + 1, upper_index, value)
        return -1


def main():
    numbers = [1, 2, 5, 7, 22, 55, 56, 99]
    binary_search = BinarySearch()
    print(binary_search.search(numbers, 0, len(numbers), 4))
    print(binary_search.search(numbers, 0, len(numbers), 2))
    print(binary_search.search(numbers, 0, len(numbers), 99))


if __name__ == '__main__':
    main()
