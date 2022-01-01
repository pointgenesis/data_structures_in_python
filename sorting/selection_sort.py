from sorting.base_sort import BaseSort


class SelectionSort(BaseSort):

    def __init__(self):
        pass

    @staticmethod
    def sort(numbers):
        for idx_outer in range(len(numbers)):
            idx_minimum = idx_outer
            for idx_inner in range(idx_outer + 1, len(numbers)):
                if numbers[idx_inner] < numbers[idx_minimum]:
                    idx_minimum = idx_inner

            numbers[idx_outer], numbers[idx_minimum] = numbers[idx_minimum], numbers[idx_outer]

        print(numbers)


if __name__ == '__main__':
    selection_sort = SelectionSort()
    selection_sort.sort([5, 1, 9, 6, 2, 8, 3, 7, 4])
