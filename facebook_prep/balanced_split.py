"""
Balanced Split
Given an array of integers (which may include repeated integers), determine if there's a way to split the array
into two subsequences A and B such that the sum of the integers in both arrays is the same, and all of the integers
in A are strictly smaller than all of the integers in B.

Note: Strictly smaller denotes that every integer in A must be less than, and not equal to, every integer in B.

Signature
bool balancedSplitExists(int[] arr)

Input
All integers in array are in the range [0, 1,000,000,000].

Output
Return true if such a split is possible, and false otherwise.

Example 1
arr = [1, 5, 7, 1]
output = true
We can split the array into A = [1, 1, 5] and B = [7].

Example 2
arr = [12, 7, 6, 7, 6]
output = false
We can't split the array into A = [6, 6, 7] and B = [7, 12] since this doesn't satisfy the requirement that all
integers in A are smaller than all integers in B.
"""

from typing import List


cache_sums_left = {}
cache_sums_right = {}


def cache_sums(my_array: List[int]) -> None:
   
    for key_index in range(len(my_array)):
        # --> right
        key_sum = 0
        for items_index in range(key_index, len(my_array)):
            key_sum += my_array[items_index]
        cache_sums_right[key_index] = key_sum
   
        # <-- left
        key_sum = 0
        for items_index in range(key_index, -1, -1):
            key_sum += my_array[items_index]
        cache_sums_left[key_index] = key_sum


def has_valid_subarrays(my_array: List[int], balance_point: int) -> bool:
    is_valid = False
   
    if my_array[balance_point] < my_array[balance_point + 1]:
        is_valid = True
   
    return is_valid


def has_equal_subarrays(my_array: List[int], balance_point: int) -> bool:
    is_valid = False
   
    left_sum = cache_sums_left[balance_point]
    right_sum = cache_sums_right[balance_point + 1]
    print(f'left_sum: {left_sum} right_sum: {right_sum}')
    if left_sum == right_sum:
        is_valid = has_valid_subarrays(my_array, balance_point)
       
    return is_valid


def is_balanced(my_array: List[int]) -> bool:
    is_valid = False
   
    my_array.sort()
   
    cache_sums(my_array)
   
    balance_point = len(my_array) // 2
   
    left_sum = cache_sums_left[balance_point]
    right_sum = cache_sums_right[balance_point + 1]
   
    if left_sum > right_sum:
        print("left heavy")
        # move balance point to left
        for index in range(balance_point - 1, 0, -1):
            is_valid = has_equal_subarrays(my_array, index) and has_valid_subarrays(my_array, index)
           
            if is_valid:
                break
       
    elif left_sum < right_sum:
        print("right heavy")
        # move balance point to right
        for index in range(balance_point + 1, len(my_array) - 1):
            is_valid = has_equal_subarrays(my_array, index) and has_valid_subarrays(my_array, index)
           
            if is_valid:
                break
    else:
        is_valid = has_equal_subarrays(my_array, balance_point) and has_valid_subarrays(my_array, balance_point)
   
    return is_valid


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def printString(string):
  print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


def main() -> None:
    my_array = [3, 1, 1, 6, 1]
    expected = True
    output = is_balanced(my_array)
    check(expected, output)

    arr_1 = [2, 1, 2, 5]
    expected_1 = True
    output_1 = is_balanced(arr_1)
    check(expected_1, output_1)

    arr_2 = [3, 6, 3, 4, 4]
    expected_2 = False
    output_2 = is_balanced(arr_2)
    check(expected_2, output_2)

if __name__ == '__main__':
    main()
