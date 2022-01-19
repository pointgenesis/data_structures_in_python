from typing import List


class StringPatternMatcher:

    def __init__(self, pattern: str) -> None:
        self.occurrences = {}
        self.pattern = pattern
        self.index_pattern(pattern)

    def index_pattern(self, pattern: str) -> None:
        index_at = [-1]
        for index, char in enumerate(pattern):
            print(f'index: {index} char: {char}')
            if char in self.occurrences:
                # get existing list of indexes
                # then add current index to indexes via append
                index_at = self.occurrences[char]
                index_at.append(index)
            else:
                # add new list
                index_at = [index]
                # add to map
                self.occurrences[char] = index_at

        print(f'{self.occurrences}')

    def check_indices(self, value: str) -> List[int]:
        matching_indices = []

        if not value:
            return matching_indices

        key = value[0]
        if key in self.occurrences:
            index_at = self.occurrences[key]
            for index in index_at:
                if index + len(value) <= len(self.pattern):
                    if value == self.pattern[index:index + len(value)]:
                        matching_indices.append(index)

        return matching_indices


def main():
    values = ['is', 'long']
    pattern = "this is my long sentence"
    matcher = StringPatternMatcher(pattern)
    for value in values:
        print(f'value: {value}')
        index_locations = matcher.check_indices(value)
        print(f'The following indexes match: {index_locations}')


if __name__ == '__main__':
    main()
