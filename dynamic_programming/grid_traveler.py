class GridTraveler:
    """
    Given a grid of M x N dimensions.
    You start in the upper left corner.
    You are allowed to move down one grid or right one grid until you reach the opposite corner.
    How many moves will be required to traverse to the opposite corner?
     _______________________
    |start|     |     |     |
     ------------------------
    |     |     |     | end |
     _______________________

    """
    def travel(self, rows, columns, cache=None):

        if cache is None:
            cache = {}

        key = f'{rows}:{columns}'
        compliment_key = f'{columns}:{rows}'
        if key in cache:
            return cache[key]

        if rows == 1 and columns == 1:
            return 1
        elif rows == 0 or columns == 0:
            return 0

        cache[key] = self.travel(rows - 1, columns, cache) + self.travel(rows, columns - 1, cache)
        cache[compliment_key] = self.travel(rows, columns - 1, cache) + self.travel(rows - 1, columns, cache)
        return cache[key]


def main():
    grid_traveler = GridTraveler()
    print(f'moves: {grid_traveler.travel(0, 0)}')
    print(f'moves: {grid_traveler.travel(0, 1)}')
    print(f'moves: {grid_traveler.travel(1, 0)}')
    print(f'moves: {grid_traveler.travel(100, 0)}')
    print(f'moves: {grid_traveler.travel(3, 3)}')
    print(f'moves: {grid_traveler.travel(10, 10)}')
    print(f'moves: {grid_traveler.travel(25, 25)}')


if __name__ == '__main__':
    main()