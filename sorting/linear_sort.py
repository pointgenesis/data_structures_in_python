class LinearSort:
    """
    Currently, this only works for positive numbers, non-duplicate values, so more work is needed to get this
    working in all scenarios.
    """

    def findNthLargestItem(self, values, nth_highest_index):
        left_index = 0
        right_index = len(values) - 1
        while left_index <= right_index:
            pivot_index = self.partition(values, left_index, right_index)
            if pivot_index == len(values) - nth_highest_index:
                return values[pivot_index]
            elif pivot_index > len(values) - nth_highest_index:
                right_index = pivot_index - 1
            else:
                left_index = pivot_index + 1
        return -1

    def partition(self, values, left_index, right_index):
        pivot_point = values[right_index]
        starting_index = left_index
        for current_index in range(left_index, right_index):
            if values[current_index] <= pivot_point:
                values[starting_index], values[current_index] = values[current_index], values[starting_index]
                starting_index += 1

        values[starting_index], values[right_index] = values[right_index], values[starting_index]
        print(values)
        return starting_index


def main():
    # values = [3, 55, 2, -1, -44, 3, 2, 1, 4, 88, 4, 88] <= breaks on negative and/or duplicated values
    values = [3, 55, 2, 1, 4, 88]
    n = 5
    linear_sort = LinearSort()
    print(f'{n}th largest value: {linear_sort.findNthLargestItem(values, 4)}')


if __name__ == '__main__':
    main()
