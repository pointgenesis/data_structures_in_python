from sorting.base_sort import BaseSort


class BubbleSort(BaseSort):

    def __init__(self):
        pass

    @staticmethod
    def sort(numbers):
        for idx_left in range(len(numbers)):
            for idx_right in range(len(numbers) - 1, -1, -1):
                print(numbers[idx_right])
                if idx_right > 0 and numbers[idx_right] > numbers[idx_right - 1]:
                    numbers[idx_right], numbers[idx_right - 1] = numbers[idx_right - 1], numbers[idx_right]

        print(numbers)


if __name__ == '__main__':
    BubbleSort.sort([5, 6, 3, 1, 4, 7, 2])
