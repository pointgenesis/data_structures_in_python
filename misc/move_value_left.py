from typing import List


def collect_values_to_left(arr: List[int], value: int = 0) -> None:
    index_sorted, index_not_sorted = 0, 0

    while index_not_sorted < len(arr):
        if arr[index_not_sorted] == value:
            arr[index_sorted], arr[index_not_sorted] = arr[index_not_sorted], arr[index_sorted]
            index_sorted += 1
        index_not_sorted += 1


def main():
    arr = [3, 5, 7, 0, 2, 0, 1, 9, 0]
    collect_values_to_left(arr)
    print(arr)

    collect_values_to_left(arr, 1)
    print(arr)

    collect_values_to_left(arr, 9)
    print(arr)


if __name__ == '__main__':
    main()
