import random

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.visited = [[False for _ in range(cols)] for _ in range(rows)]
        self.stack = []

    def generate(self, row=0, col=0):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        self.visited[row][col] = True
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and not self.visited[nr][nc]:
                self.grid[row][col] |= self._dir_to_bit(dr, dc)
                self.grid[nr][nc] |= self._dir_to_bit(-dr, -dc)
                self.generate(nr, nc)

    def _dir_to_bit(self, dr, dc):
        return {
            (0, 1): 1,  # Right
            (1, 0): 2,  # Down
            (0, -1): 4, # Left
            (-1, 0): 8, # Up
        }[(dr, dc)]

    def get_grid(self):
        return self.grid
