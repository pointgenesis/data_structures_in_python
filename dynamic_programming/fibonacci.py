class Fibonacci:

    def calc(self, number, cache=None):
        if cache is None:
            cache = {}

        if number in cache:
            return cache[number]

        if number <= 2:
            cache[number] = 1
            return cache[number]

        cache[number] = self.calc(number - 1, cache) + self.calc(number - 2, cache)

        return cache[number]


def main():
    fib = Fibonacci()
    print(fib.calc(50))


if __name__ == '__main__':
    main()
