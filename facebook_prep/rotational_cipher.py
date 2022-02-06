"""Rotational Cipher
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. 
Rotating a character means replacing it with another character that is a certain number of steps away in normal 
alphabetic or numerical order.

For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". 
Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and 
every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the 
non-alphanumeric characters remain unchanged.

Given a string and a rotation factor, return an encrypted string.

Signature
string rotationalCipher(string input, int rotationFactor)

Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000

Output
Return the result of rotating input a number of times equal to rotationFactor.

Example 1
input = Zebra-493?
rotationFactor = 3
output = Cheud-726?
Example 2
input = abcdefghijklmNOPQRSTUVWXYZ0123456789
rotationFactor = 39
output = nopqrstuvwxyzABCDEFGHIJKLM9012345678"""

import math


# Add any extra import statements you may need here


# Add any helper functions you may need here
LOWERCASE_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
alpha_numeric_cache = {}
IS_DEBUG = False


def calculate_offset(rotation_factor: int, alphabet: str) -> int:
    if rotation_factor > 0:
        return rotation_factor % len(alphabet)


def get_index(value: str, values: str) -> int:
    if value in alpha_numeric_cache:
        return alpha_numeric_cache[value]

    for index, char in enumerate(values):
        print(f'value: {value} char: {char} -> index: {index}') if IS_DEBUG else None
        if value == char:
            alpha_numeric_cache[char] = index
            return alpha_numeric_cache[char]

    return -1


def calculate_new_index(index: int, offset_factor: int, alphabet: str) -> str:
    desired_index = index + offset_factor

    if desired_index > len(alphabet) - 1:
        desired_index -= len(alphabet)

    print(f'index: {index} offset_factor: {offset_factor} desired_index: {desired_index} alphabet: {alphabet}') if IS_DEBUG else None

    return alphabet[desired_index]


def is_lowercase_alphabet(digit: str) -> bool:
    if digit in LOWERCASE_ALPHABET:
        print(f'is_lowercase_alphabet: {digit}') if IS_DEBUG else None
        return True
    return False


def is_uppercase_alphabet(digit: str) -> bool:
    if digit in UPPERCASE_ALPHABET:
        print(f'is_uppercase_alphabet: {digit}') if IS_DEBUG else None
        return True
    return False


def is_numeric(digit: str) -> bool:
    if digit in NUMBERS:
        print(f'is_numeric: {digit}') if IS_DEBUG else None
        return True
    print(f'NOT is_numeric: {digit}') if IS_DEBUG else None
    return False


def rotational_cipher(values, rotation_factor):
    alpha_offset_factor = calculate_offset(rotation_factor, LOWERCASE_ALPHABET)
    numeric_offset_factor = calculate_offset(rotation_factor, NUMBERS)

    new_value = ""
    for index, char in enumerate(values):
        if is_lowercase_alphabet(char):
            char_index = get_index(char, LOWERCASE_ALPHABET)
            new_value += calculate_new_index(char_index, alpha_offset_factor, LOWERCASE_ALPHABET)
        elif is_uppercase_alphabet(char):
            char_index = get_index(char, UPPERCASE_ALPHABET)
            new_value += calculate_new_index(char_index, alpha_offset_factor, UPPERCASE_ALPHABET)
        elif is_numeric(char):
            char_index = get_index(char, NUMBERS)
            new_value += calculate_new_index(char_index, numeric_offset_factor, NUMBERS)
        else:
            new_value += char

    return new_value


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def print_string(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    right_tick = '\u2713'
    wrong_tick = '\u2717'
    if result:
        print(right_tick, 'Test #', test_case_number, sep='')
    else:
        print(wrong_tick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        print_string(expected)
        print(' Your output: ', end='')
        print_string(output)
        print()
    test_case_number += 1


def main():
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotational_cipher(input_1, rotation_factor_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotational_cipher(input_2, rotation_factor_2)
    check(expected_2, output_2)

    # Add your own test cases here


if __name__ == "__main__":
    main()
