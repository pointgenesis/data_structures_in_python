"""
Interview Question:

Determine whether or not a given list is a valid (min/max) heap by checking its' properties.
"""
from typing import List


class MinHeapComparator:
    def __init__(self, heap: List[int]) -> None:
        self.heap = heap
        self.heap_size = len(heap)

    def is_min_heap(self) -> bool:
        return self.heapify_down(0)

    def heapify_down(self, index: int) -> bool:
        left_index = (index * 2) + 1
        right_index = (index * 2) + 2

        # print(f'left_index: {left_index} right_index: {right_index} parent: {index} heap_size: {self.heap_size}')

        smallest_index = index

        if left_index < self.heap_size and self.heap[left_index] < self.heap[index]:
            smallest_index = left_index

        if right_index < self.heap_size and self.heap[right_index] < self.heap[smallest_index]:
            smallest_index = right_index

        if index != smallest_index:
            return False

        if left_index < self.heap_size and right_index < self.heap_size:
            return self.heapify_down(left_index) and self.heapify_down(right_index)

        return True

    def is_min_heap_alt(self, heap: List[int]) -> bool:
        item_count = (len(self.heap) - 2) // 2

        for idx in range(item_count):
            if heap[idx] > heap[(2 * idx) + 1] or heap[idx] > heap[(2 * idx) + 2]:
                return False

        return True


def main():
    values_invalid = [3, 8, 2, 0, 5, 33]
    heap_invalid = MinHeapComparator(values_invalid)
    print(heap_invalid.is_min_heap())

    values_valid = [-5, 1, -2, 13, 8, 0, 99]
    heap_valid = MinHeapComparator(values_valid)
    print(heap_valid.is_min_heap())

if __name__ == '__main__':
    main()
