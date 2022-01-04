from sorting.base_sort import BaseSort


class BubbleSort(BaseSort):

    def __init__(self):
        pass

    @staticmethod
    def sort(numbers):
        for idx_left in range(len(numbers)):
            for idx_right in range(len(numbers) - 1, -1, -1):
                if idx_right > 0 and numbers[idx_right] < numbers[idx_right - 1]:
                    numbers[idx_right], numbers[idx_right - 1] = numbers[idx_right - 1], numbers[idx_right]

        print(numbers)


if __name__ == '__main__':
    values = [5, 6, 3, 1, 4, 7, 2]
    BubbleSort.sort(values)
    print(values)

    # from misc.person import Person
    # travis = Person('travis', 50)
    # jennifer = Person('jennifer', 50)
    # erin = Person('erin', 29)
    # jordan = Person('jordan', 26)
    # caleb = Person('caleb', 23)
    # spencer = Person('spencer', 23)
    #
    # persons = [jordan, jennifer, spencer, travis, caleb, erin]
    #
    # BubbleSort.sort(persons)

    listA = [0]
    listB = listA
    listB.append(1)
    print(listA)
    print(listB)
    print(hex(id(listB)) == hex(id(listA)))
    print(hex(id(listB)))
    print(hex(id(listA)))
