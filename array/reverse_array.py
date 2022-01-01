class ReverseArray():

    def __init__(self):
        pass

    def reverse(self, ordered_array):
        idx = 0
        head_idx = idx
        tail_idx = len(ordered_array) - 1
        midpoint = len(ordered_array) // 2
        print(f'head_idx: {head_idx} tail_idx: {tail_idx} midpoint: {midpoint}')
        while idx < midpoint:
            head_value = ordered_array[head_idx]
            tail_value = ordered_array[tail_idx]
            print(f'head_value: {head_value} tail_value: {tail_value} idx: {idx}')

            ordered_array[tail_idx] = head_value
            ordered_array[head_idx] = tail_value
            print(f'ordered_array[tail_idx]: {ordered_array[tail_idx]}  ordered_array[head_idx]: {ordered_array[head_idx]}')

            head_idx += 1
            tail_idx -= 1
            idx += 1
            print(f'head_idx: {head_idx} tail_idx: {tail_idx} idx: {idx}')


if __name__ == '__main__':
    sorted_array = [1, 2, 3, 4, 5, 6, 7]
    reverse_array = ReverseArray()
    reverse_array.reverse(sorted_array)
    print(sorted_array)