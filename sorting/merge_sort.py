class MergeSort:

    def __init__(self, debug=False):
        self.debug = debug

    def sort(self, numbers):
        print(f'sort({numbers}) invoked') if self.debug else None
        if len(numbers) == 1:
            return

        idx_middle = len(numbers) // 2
        left_half_numbers = numbers[:idx_middle]
        right_half_numbers = numbers[idx_middle:]

        self.sort(left_half_numbers)
        self.sort(right_half_numbers)

        i, j, k = 0, 0, 0

        while i < len(left_half_numbers) and j < len(right_half_numbers):
            if left_half_numbers[i] < right_half_numbers[j]:
                numbers[k] = left_half_numbers[i]
                i += 1
            else:
                numbers[k] = right_half_numbers[j]
                j += 1
            k += 1

        while i < len(left_half_numbers):
            numbers[k] = left_half_numbers[i]
            k += 1
            i += 1

        while j < len(right_half_numbers):
            numbers[k] = right_half_numbers[j]
            k += 1
            j += 1


if __name__ == '__main__':
    initial_numbers = [99, 13, 9, 11, 1, -3, 8, 40, -2, 13, 9]
    print(initial_numbers)
    merge_sort = MergeSort()
    merge_sort.sort(initial_numbers)
    print(initial_numbers)