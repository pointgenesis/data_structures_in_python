import copy


class QuickSortHoareImpl:

    def __init__(self, unsorted_array):
        self.unsorted_array = unsorted_array
        self.debug = False

    def partition(self, idx_low, idx_high):
        # pivot = arr[low + (high - low) // 2]
        pivot = self.unsorted_array[(idx_high + idx_low) // 2]

        i = idx_low
        j = idx_high

        while True:
            print(f'check: arr[i]: {self.unsorted_array[i]} pivot: {pivot}') if self.debug else None

            while self.unsorted_array[i] < pivot:
                i += 1

            print(f'check: arr[j]: {self.unsorted_array[j]} pivot: {pivot}') if self.debug else None
            while self.unsorted_array[j] > pivot:
                j -= 1

            print(f'i: {i} j: {j}') if self.debug else None
            if i >= j:
                return j

            self.unsorted_array[i], self.unsorted_array[j] = self.unsorted_array[j], self.unsorted_array[i]

            i += 1 # <<<< Not sure how this fixes the infinite loop issue with duplicate values... but it does, so investigate
            j -= 1 # <<<< Not sure how this fixes the infinite loop issue with duplicate values... but it does, so investigate
            #reference: https://tipsfordev.com/quicksort-hoare-s-partitioning-with-duplicate-values

    def sort(self, idx_low, idx_high):
        if idx_low < idx_high:
            partition_point = self.partition(idx_low, idx_high)

            self.sort(idx_low, partition_point)
            self.sort(partition_point + 1, idx_high)

    def get_sorted_array(self) -> list:
        return self.unsorted_array


if __name__ == '__main__':
    initial_array_with_dups = [44, 44, -4, 12, -3, 88, 75, 3, 2, -4, 72]
    quick_sort_hoare = QuickSortHoareImpl(copy.copy(initial_array_with_dups))
    quick_sort_hoare.sort(0, len(initial_array_with_dups) - 1)
    print(initial_array_with_dups)
    print(quick_sort_hoare.get_sorted_array())