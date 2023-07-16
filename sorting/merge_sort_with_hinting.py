import logging
from typing import List

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

log = logging.getLogger(__name__)


class MergeSort:
    def __init__(self):
        log.debug('initializing')

    def sort(self, unsorted_values) -> List[int]:
        log.debug(f'{unsorted_values}')

        array_length = len(unsorted_values)
        if array_length == 1:
            log.debug(f'hit the bottom: {unsorted_values}')
            return unsorted_values

        middle_index: int = len(unsorted_values) // 2
        log.debug(f'middle_index: {middle_index}')

        left_values: List[int] = self.sort(unsorted_values[0:middle_index])
        right_values: List[int] = self.sort(unsorted_values[middle_index:])

        log.debug(f'{left_values}:{right_values}')

        left_index: int = 0
        right_index: int = 0

        sorted_values: List[int] = []
        while right_index < len(right_values) and left_index < len(left_values):
            if right_values[right_index] <= left_values[left_index]:
                sorted_values.append(right_values[right_index])
                right_index += 1
            elif right_values[right_index] > left_values[left_index]:
                sorted_values.append(left_values[left_index])
                left_index += 1

        while right_index < len(right_values):
            sorted_values.append(right_values[right_index])
            right_index += 1

        while left_index < len(left_values):
            sorted_values.append(left_values[left_index])
            left_index += 1

        return sorted_values


def main() -> None:
    unsorted_values: List[int] = [99, 13, 9, 11, 1, -3, 8, 40, -2, 13, 9]  # [4,2,5,9,3]
    merge_sort: MergeSort = MergeSort()
    log.info(f'sorted_values: {merge_sort.sort(unsorted_values)}')


if __name__ == '__main__':
    main()