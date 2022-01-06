import copy
from typing import List


class QuickSortLomuto:

    def __init__(self, unsorted_array):
        self.unsorted_array = unsorted_array

    def partition(self, idx_left: int, idx_right: int) -> int:

        idx_pivot = (idx_left + idx_right) // 2

        self.unsorted_array[idx_pivot], self.unsorted_array[idx_right] = self.unsorted_array[idx_right], \
            self.unsorted_array[idx_pivot]

        for idx in range(idx_left, idx_right):
            if self.unsorted_array[idx] <= self.unsorted_array[idx_right]:
                self.unsorted_array[idx_left], self.unsorted_array[idx] = self.unsorted_array[idx], \
                    self.unsorted_array[idx_left]
                idx_left += 1

        self.unsorted_array[idx_left], self.unsorted_array[idx_right] = self.unsorted_array[idx_right], \
            self.unsorted_array[idx_left]

        return idx_left

    def sort(self, idx_left: int, idx_right) -> None:
        if idx_left >= idx_right:
            return

        partition_point = self.partition(idx_left, idx_right)
        self.sort(idx_left, partition_point - 1)
        self.sort(partition_point + 1, idx_right)

    def get_sorted_array(self) -> List[int]:
        return self.unsorted_array


if __name__ == '__main__':
    initial_array_with_dups = [44, 44, -4, 12, -3, 88, 75, 3, 2, -4, 72]
    quick_sort_lomuto = QuickSortLomuto(copy.copy(initial_array_with_dups))
    quick_sort_lomuto.sort(0, len(initial_array_with_dups) - 1)
    print(initial_array_with_dups)
    print(quick_sort_lomuto.get_sorted_array())
