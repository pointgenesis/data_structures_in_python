class MergeSort:

    def __init__(self):
        pass

    def merge(self, array_sorted_1, array_sorted_2, array_merged):
        idx_sorted_1, idx_sorted_2, idx_merged = 0, 0, 0

        while idx_sorted_1 < len(array_sorted_1) and idx_sorted_2 < len(array_sorted_2):
            if array_sorted_1[idx_sorted_1] < array_sorted_2[idx_sorted_2]:
                array_merged.append(array_sorted_1[idx_sorted_1])
                idx_sorted_1 += 1
            else:
                array_merged.append(array_sorted_2[idx_sorted_2])
                idx_sorted_2 += 1
            idx_merged += 1

        while idx_sorted_1 < len(array_sorted_1):
            array_merged.append(array_sorted_1[idx_sorted_1])
            idx_sorted_1 += 1
            idx_merged += 1

        while idx_sorted_2 < len(array_sorted_2):
            array_merged.append(array_sorted_2[idx_sorted_2])
            idx_sorted_2 += 1
            idx_merged += 1


if __name__ == '__main__':
    arr_sorted_1 = [1, 2, 19, 32, 55]
    arr_sorted_2 = [3, 7, 21, 33, 42, 54]
    arr_merged = []
    merge_sort = MergeSort()
    merge_sort.merge(arr_sorted_1, arr_sorted_2, arr_merged)
    print(arr_merged)
