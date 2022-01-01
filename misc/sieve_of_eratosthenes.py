from typing import List


class SieveOfEratosthenes:

    def __init__(self):
        print('Initializing SieveOfEratosthenes...')

    def reduce_to_primes(self, max_input: int) -> List[int]:

        primes = [True for i in range(max_input+1)]

        value = 2
        while value * value <= max_input:
            if primes[value]:
                for i in range(value * value, max_input + 1, value):
                    primes[i] = False
            value += 1

        return self.compress_primes(primes, max_input)

    def compress_primes(self, commingled_list: List[int], end_index) -> List[int]:
        primes = []
        for index in range(2, end_index + 1):
            if commingled_list[index]:
                primes.append(index)

        return primes


if __name__ == '__main__':
    soe = SieveOfEratosthenes()
    print(soe.reduce_to_primes(10))
    print(soe.reduce_to_primes(20))
