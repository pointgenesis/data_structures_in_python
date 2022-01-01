from sorting.base_sort import BaseSort


class InsertionSort(BaseSort):

    def __init__(self):
        pass

    @staticmethod
    def sort(numbers):
        for idx_outer in range(1, len(numbers)):
            tmp_data_point = numbers[idx_outer]
            idx_inner = idx_outer
            while idx_inner > 0 and numbers[idx_inner - 1] >= tmp_data_point:
                numbers[idx_inner] = numbers[idx_inner - 1]
                idx_inner -= 1

            numbers[idx_inner] = tmp_data_point

        print(numbers)


if __name__ == '__main__':
    InsertionSort.sort([5, 1, 9, 6, 2, 8, 3, 7, 4])
