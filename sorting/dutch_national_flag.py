"""
Given an unsorted one-dimensional array with range values 0, 1, 2.
Find a linear time complexity solution for sorting.

"""
values = [0, 2, 2, 0, 1, 0, 1, 1, 0, 0, 2]
print(f'sorted values: {values}')

MIDDLE_VALUE = 1
left_index = 0
float_index = 0
right_index = len(values) - 1
while float_index <= right_index:
    print(f'left_index: {left_index} float_index: {float_index} right_index: {right_index}')
    print(f'{values}')
    if values[float_index] < MIDDLE_VALUE:
        # means that the current value under inspection is 0
        values[left_index], values[float_index] = values[float_index], values[left_index]
        left_index += 1
        float_index += 1
    elif values[float_index] > MIDDLE_VALUE:
        # means that the current value under inspection is 2
        values[right_index], values[float_index] = values[float_index], values[right_index]
        right_index -= 1
    else:
        # means that the current value under inspection is 1
        float_index += 1
    print(f'{values}')
print(f'sorted values: {values}')