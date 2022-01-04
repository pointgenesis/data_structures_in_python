import copy
from typing import List


class QuickSort:

    def __init__(self, unsorted_array):
        self.unsorted_array = unsorted_array

    def partition(self, idx_left: int, idx_right: int, pivot_point: int) -> int:
        left_pointer = idx_left
        right_pointer = idx_right - 1

        while True:
            while self.unsorted_array[left_pointer] < pivot_point:
                left_pointer += 1

            while right_pointer > 0 and self.unsorted_array[right_pointer] > pivot_point:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
            else:
                self.unsorted_array[left_pointer], self.unsorted_array[right_pointer] = \
                    self.unsorted_array[right_pointer], self.unsorted_array[left_pointer]

        self.unsorted_array[left_pointer], self.unsorted_array[idx_right] = self.unsorted_array[idx_right], \
            self.unsorted_array[left_pointer]
        return left_pointer

    def sort(self, idx_left: int, idx_right) -> None:
        # print(f'idx_left: {idx_left} idx_right: {idx_right}')

        if idx_right - idx_left > 0:
            pivot_point = self.unsorted_array[idx_right]

            partition_point = self.partition(idx_left, idx_right, pivot_point)

            self.sort(idx_left, partition_point - 1)
            self.sort(partition_point + 1, idx_right)

    def get_sorted_array(self) -> List[int]:
        return self.unsorted_array


if __name__ == '__main__':
    initial_array = [44, 12, -3, 88, 75, 3, 2, -4, 72]
    quick_sort = QuickSort(copy.copy(initial_array))
    quick_sort.sort(0, len(initial_array) - 1)
    print(initial_array)
    print(quick_sort.get_sorted_array())
