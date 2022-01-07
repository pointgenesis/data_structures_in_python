class ShellSort:

    def __init__(self):
        pass

    def sort(self, unsorted_array):
        """ This can be based on either the insertion sort or bubble sort algorithm """

        # Knuth's Formula => h = (h * 3) + 1
        h = 1
        while h <= len(unsorted_array) // 3:
            h = (h * 3) + 1

        # idx_outer, idx_inner = 0, 0
        while h > 0:
            for idx_outer in range(h, len(unsorted_array), 1):
                data_point = unsorted_array[idx_outer]
                idx_inner = idx_outer
                while idx_inner > h - 1 and unsorted_array[idx_inner - h] >= data_point:
                    unsorted_array[idx_inner] = unsorted_array[idx_inner - h]
                    idx_inner -= h
                unsorted_array[idx_inner] = data_point
            h = (h - 1) // 3


if __name__ == '__main__':
    array_unsorted = [44, 8, 22, 1, 11, 89, 33, 23, 7, 90, 7, 8, -23, 25]
    print(f'before: {array_unsorted}')
    shell_sort = ShellSort()
    shell_sort.sort(array_unsorted)
    print(f'after: {array_unsorted}')
