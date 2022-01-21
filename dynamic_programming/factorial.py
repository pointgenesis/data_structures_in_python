class Factorial:
    def __init__(self):
        pass

    def factorial(self, value):
        if value == 1 or value == 0:
            return 1

        return value * self.factorial(value - 1)


def main():
    fac = Factorial()
    print(fac.factorial(100))


if __name__ == '__main__':
    main()
