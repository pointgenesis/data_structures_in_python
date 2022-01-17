from typing import List

CAPACITY = 10


class MinHeap:

    def __init__(self) -> None:
        self.heap_size: int = 0
        self.heap: List[int] = [0] * CAPACITY

    def insert(self, item: int) -> None:
        if self.heap_size == CAPACITY:
            return

        self.heap[self.heap_size] = item
        self.heap_size += 1

        self.heapify_up(self.heap_size - 1)

    def heapify_down(self, index: int) -> None:
        left_index = (index * 2) + 1
        right_index = (index * 2) + 2

        smallest_index = index

        if left_index < self.heap_size and self.heap[left_index] < self.heap[index]:
            smallest_index = left_index

        if right_index < self.heap_size and self.heap[right_index] < self.heap[smallest_index]:
            smallest_index = right_index

        if index != smallest_index:
            self.heap[smallest_index], self.heap[index] = self.heap[index], self.heap[smallest_index]
            self.heapify_down(smallest_index)

    def heapify_up(self, index: int) -> None:
        # in a heap the parent has index = i, then the left child index is 2i + 1, and the right child index is 2i + 2
        # or given a child the parent has index = (idx - 1) // 2 (if index is a left child)
        # or given a child the parent has index = (idx - 2) // 2 (if index is a right child)
        # i.e., 3 (left child) => (3 - 1) // 2 => 2
        # i.e., 4 (right child) => (4 - 2) // 2 => 2
        # observation: to minimize code it is observed that (4 - 1) // 2 => 3 // 2 => 2, so only the left child formula
        # needs to be checked to arrive at the parent
        parent_index = (index - 1) // 2

        if index > 0 and self.heap[index] < self.heap[parent_index]:
            # swap the values
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # compare parent to its' parent
            self.heapify_up(parent_index)

    def peek_at_min(self) -> int:
        return self.heap[0]

    def pop_min(self) -> int:
        min_item = self.peek_at_min()
        # print(f'BEFORE: max_item: {max_item} -> leaf: {self.heap[self.heap_size - 1]}')
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        # print(f'AFTER: max_item: {max_item} -> leaf: {self.heap[self.heap_size - 1]}')
        self.heap_size -= 1

        self.heapify_down(0)

        return min_item

    def heap_sort(self, asc_values: List[int] = None) -> List[int]:
        if asc_values is None:
            asc_values = [0] * self.heap_size

        for index in range(self.heap_size):
            # print(f'{index}:{self.heap_size}')
            asc_values[index] = self.pop_min()

        return asc_values


def main():
    heap = MinHeap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(99)
    print(heap.heap)
    print(heap.heap_size)
    print(heap.heap_sort())


if __name__ == '__main__':
    main()
