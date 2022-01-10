class LinearSort:
    """
    Currently, this only works for positive numbers, non-duplicate values, so more work is needed to get this
    working in all scenarios.
    """

    def find_nth_largest_item(self, values, nth_highest_index):
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

    def min(self, values):
        return self.find_nth_largest_item(values, len(values))

    def max(self, values):
        largest_valued_item = 1
        return self.find_nth_largest_item(values, largest_valued_item)


def main():
    # values = [3, 55, 2, -1, -44, 3, 2, 1, 4, 88, 4, 88] <= breaks on negative and/or duplicated values
    values = [3, 55, 2, 1, 4, 88]
    n = 2
    linear_sort = LinearSort()
    print(f'{n}th largest value: {linear_sort.find_nth_largest_item(values, n)}')
    print(f'min value: {linear_sort.min(values)}')
    print(f'max value: {linear_sort.max(values)}')


if __name__ == '__main__':
    main()
