import random
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


class RadixSort:

    def __init__(self, data):
        self.data = data
        self.ITEMS_IN_BUCKET = 10

    def get_digits(self):
        return len(str(max(self.data)))

    def sort(self):
        for digit in range(self.get_digits()):
            self.counting_sort(digit)

    def counting_sort(self, d):

        count_array = [[] for _ in range(self.ITEMS_IN_BUCKET)]

        # store the count of each element in count array O(N)
        for num in self.data:
            # calculate the index of the given bucket
            index = (num // (10 ** d)) % 10
            count_array[index].append(num)

        # we have to consider all the items in the count array (list)
        z = 0
        for i in range(len(count_array)):
            while len(count_array[i]) > 0:
                # it takes O(N) linear running time complexity - dictionary O(1)
                self.data[z] = count_array[i].pop(0)
                z += 1


if __name__ == '__main__':

    n = [5, 3, 10, 12, 9, 8, 20, 100, 325, 1023]
    random.shuffle(n)
    print(n)
    radix_sort = RadixSort(n)
    radix_sort.sort()
    print(radix_sort.data)