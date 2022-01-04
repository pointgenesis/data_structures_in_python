
class Person:

    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age

    def __eq__(self, other):
        return True if self.age == other.age else False

    def __gt__(self, other):
        return True if self.age > other.age else False

    def __lt__(self, other):
        return True if self.age < other.age else False

    def __ge__(self, other):
        return True if self.age >= other.age else False

    def __le__(self, other):
        return True if self.age <= other.age else False

    def __str__(self):
        return f'first_name: {self.first_name} age: {self.age}'
