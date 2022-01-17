from typing import List


asc_values = [1, 2, 3, 4, 5, 6, 7]

def reverse_array(values: List[int]) -> None:
    left_index = 0
    right_index = len(values) - 1
    while left_index < right_index:
        values[left_index], values[right_index] = values[right_index], values[left_index]
        left_index += 1
        right_index -= 1


print(asc_values)
reverse_array(asc_values)
print(asc_values)
