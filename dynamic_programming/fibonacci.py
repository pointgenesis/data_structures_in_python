# fib = [0, 1, 1, 2, 3, 5, 8, 13... ]

# Problem: Given a position determine the Fibonacci value.
# Issue: Fibonacci is an exponential growth algorithm, so incorporate a cache mechanism

class Fibonacci:
    def __ini__(self):
        self.cache = {}
        position = 0
        self.cache[0] = 0
        print(self.cache.items())

        if 0 in self.cache:
            print(self.cache[position])
        # consider a cache limiting routine to keep the cache below a certain size to prevent a memory leak via unbounded growth

    def value_at_index(self, position: int) -> int:
        """ The fibonacci sequence starts at index: 0 value: 0 => position = index """
        if position in self.cache:
            return self.cache[position]

        if position == 0:
            self.cache[position] = 0
            return self.cache[position]
        elif position <= 2:
            self.cache[position] = 1
            return self.cache[position]
        else:
            self.cache[position] = self.value_at_index(position - 1) + self.value_at_index(position - 2)
            return self.cache[position]


def main():
    fib = Fibonacci()
    # for position in range(0, 10):
    #     print(fib.value_at_index(position))


if __name__ == '__main__':
    main()
