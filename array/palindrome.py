class Palindrome:

    def __init__(self):
        pass

    def check_for_conformance(self, value):
        print(f'Examining value: {value}')
        value = value.lower()

        idx = 0
        middle_idx = len(value) // 2
        end_idx = len(value) - 1

        while idx <= middle_idx:
            if value[idx] == value[end_idx]:
                print(f'value[{idx}]: {value[idx]} == value[{end_idx}]: {value[end_idx]}')
            else:
                return False
            # end if
            idx += 1
            end_idx -= 1
        # end while
        return True
    # end def


if __name__ == '__main__':
    palindrome = Palindrome()
    word = 'radar'
    print(f'Is the word, {word}, a palindrome? Answer: {palindrome.check_for_conformance(word)}')

    word = 'madam'
    print(f'Is the word, {word}, a palindrome? Answer: {palindrome.check_for_conformance(word)}')

    word = 'redivider'
    print(f'Is the word, {word}, a palindrome? Answer: {palindrome.check_for_conformance(word)}')

    word = 'Hannah'
    print(f'Is the word, {word}, a palindrome? Answer: {palindrome.check_for_conformance(word)}')