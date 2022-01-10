class Fibonacci:

    def calc(self, number):
        cache = {}
        return self.fib_sequence(number, cache)

    def fib_sequence(self, number, cache):
        if number in cache:
            return cache[number]

        if number <= 2:
            cache[number] = 1
            return cache[number]

        cache[number] = self.fib_sequence(number - 1, cache) + self.fib_sequence(number - 2, cache)

        return cache[number]


def main():
    fib = Fibonacci()
    print(fib.calc(75))


if __name__ == '__main__':
    main()
