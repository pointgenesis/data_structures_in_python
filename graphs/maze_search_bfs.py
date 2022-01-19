from collections import deque  # doubly-linked list


class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        # D(0, 1) U(0, -1), L(-1, 0) R(1, 0)
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        self.visited = [[False for _ in range(len(maze))] for _ in range(len(maze))]
        self.minimum_distance = float('inf')

    def is_valid(self, row, column):
        if row < 0 or row >= len(self.maze):
            return False  # Outside left/right boundary

        if column < 0 or column >= len(self.maze):
            return False  # Outside top/bottom boundary

        if self.maze[row][column] == 0:
            return False  # WALL - cannot go through a wall

        if self.visited[row][column]:
            return False

        return True

    def search(self, start_x, start_y, destination_x, destination_y):
        self.visited[start_x][start_y] = True
        queue = deque()
        queue.append([start_x, start_y, 0])
        while queue:
            # first item inserted
            (start_x, start_y, distance) = queue.popleft()

            # break out if we reach the destination
            if start_x == destination_x and start_y == destination_y:
                self.minimum_distance = distance
                break

            for move in range(len(self.move_x)):
                next_x = start_x + self.move_x[move]
                next_y = start_y + self.move_y[move]
                print(f'next_x: {next_x} next_y: {next_y}')

                if self.is_valid(next_x, next_y):
                    self.visited[next_x][next_y] = True
                    queue.append((next_x, next_y, distance + 1))


    def show_result(self):
        if self.minimum_distance != float('inf'):
            print(f'The shortest path from source to destination is: {self.minimum_distance}')
        else:
            print(f'The destination cannot be reached!')


def main():
    maze = [
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1],
    ]

    maze_solver = MazeSolver(maze)
    maze_solver.search(0, 0, 4, 4)
    maze_solver.show_result()


if __name__ == '__main__':
    main()
