from typing import List


class CountingSort:

    def __init__(self, unsorted_numbers: List[int], debug: bool = False) -> None:
        self.unsorted_numbers = unsorted_numbers
        self.debug = debug
        self.presorted_numbers = [0] * (max(self.unsorted_numbers) - min(self.unsorted_numbers) + 1)

    def sort(self) -> List[int]:
        for number in self.unsorted_numbers:
            print(f'number: {number}') if self.debug else None
            # The min and/or max values may be negative integers and/or very far apart introducing additional
            # complications, so we can mitigate this by adjusting the indices down by the min() value of the original
            # dataset, i.e., min(self.unsorted_numbers)
            self.presorted_numbers[number - min(self.unsorted_numbers)] += 1
            print(f'count at index({number - 1}): {self.presorted_numbers[number - 1]}') if self.debug else None

        sorted_array = []
        for index, number in enumerate(self.presorted_numbers):
            if self.presorted_numbers[index] > 0:
                for value in range(self.presorted_numbers[index]):
                    # remember to undo the minimum value adjustment made above by adding the min value back
                    sorted_array.append(index + min(self.unsorted_numbers))

        return sorted_array


if __name__ == '__main__':
    before = [1, 4, 1, 7, 1, 10, 3, -2, -22]
    print(f'before: {before}')
    counting_sort = CountingSort(before)
    after = counting_sort.sort()
    print(f'after: {after}')
