class ReverseOrder:

    def __init__(self):
        pass
    # __init__

    def reverse(self, sentence):
        print(f'sentence: {sentence}')
        new_sentence = ''
        words = sentence.split()
        for word in words:
            # print(f'word: {word}')
            reversed_word = ''
            for character in word:
                # print(f'character: {character}')
                if character in ['.', '?', '!']:
                    reversed_word = reversed_word + character
                else:
                    reversed_word = character + reversed_word
                # if character
            # for character
            new_sentence = f'{new_sentence} {reversed_word}'
        # for word
        return new_sentence
    # inspect


if __name__ == '__main__':
    reverse_order = ReverseOrder()
    print(reverse_order.reverse('This is a sentence to reverse.'))
    print(reverse_order.reverse('This is super-duper trooper!'))
    print(reverse_order.reverse(',:;.-!'))
# if

# class
