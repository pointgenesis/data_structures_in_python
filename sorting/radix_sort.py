class RadixSort:

    def __init__(self, dataset, debug: bool = False) -> None:
        self.dataset = dataset
        self.debug = debug

    def __sort__(self):
        pass

if __name__ == '__main__':
    numbers = [99392, 2, 5, 53, 305, 33, 632, 9933, 2222]
    radix_sort = RadixSort(numbers)

