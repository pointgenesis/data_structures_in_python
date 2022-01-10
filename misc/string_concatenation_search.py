class WordConcatenation:
    def __init__(self, debug=False):
        self.debug = debug

    def discover_word_concatenations(self, words):
        cached_words = {}
        return [word for word in words if self.is_word_found(word, words, cached_words)]

    def is_word_found(self, word, unique_words, cached_words):
        print(word) if self.debug else None
        print(cached_words) if self.debug else None
        if word in cached_words:
            print(f'found in cached_words: {word}') if self.debug else None
            return cached_words[word]

        for index in range(1, len(word)):
            prefix = word[:index]
            suffix = word[index:]
            if prefix in unique_words:
                if suffix in unique_words or self.is_word_found(suffix, unique_words, cached_words):
                    cached_words[word] = True
                    return True
        cached_words[word] = False
        return False


def main():
    words = ["fish", "dogfish", "fish", "dog"]
    word_concatenation = WordConcatenation()
    print(word_concatenation.discover_word_concatenations(words))


if __name__ == "__main__":
    main()
