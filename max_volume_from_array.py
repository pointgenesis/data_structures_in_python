numbers = [1, 3, 9, 2, 1]

outer_index = 0
inner_index = 1
max_volume = -1

while outer_index < len(numbers):
    print(numbers[outer_index])

    while inner_index < len(numbers):
        print(numbers[inner_index])

        distance = inner_index - outer_index
        if numbers[inner_index] >= numbers[outer_index]:
            volume = numbers[outer_index] * distance
        else:
            volume = numbers[inner_index] * distance

        if volume >= max_volume:
            max_volume = volume
            max_volume_inner_idx = inner_index
            max_volume_outer_idx = outer_index
        else:
            print(f'volume: {volume} is less than max_volume: {max_volume}')

        inner_index += 1

    outer_index += 1
    inner_index = outer_index

print(f'max_volume: {max_volume} outer_index: {max_volume_outer_idx} inner_index: {max_volume_inner_idx}')
