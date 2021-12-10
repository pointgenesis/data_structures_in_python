class Anagram:

    def __init__(self):
        pass

    def compare(self, word1, word2):
        array1 = (list(word1))
        array2 = list(word2)

        array1.sort()
        array2.sort()

        print(f'array1: {array1} array2: {array2}')

        if len(array1) == len(array2):
            idx = 0
            while idx < len(array1):
                if array1[idx] != array2[idx]:
                    return False
                idx += 1
            return True
        else:
            return False


if __name__ == '__main__':
    words = ['fluster', 'restful']
    anagram = Anagram()
    answer = anagram.compare(words[0], words[1])
    print(f"Are words {words[0]} {words[1]} an anagram? Answer: {answer}")
