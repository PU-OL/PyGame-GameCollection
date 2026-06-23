import pygame
import random
from collections import deque
from cell_class import cell

UP, RIGHT, DOWN, LEFT = 0,1,2,3

class levelgeneration():
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows

        self.grid = []
        self.reset()

    def loading_screen(self, screen, tries):
        screen.fill("black")

        font = pygame.font.SysFont("Arial", 36)
        text = font.render("Labyrinth gets generated. Please wait.", True, (255, 0, 0))
        screen.blit(text, (50, 50))
        text = font.render(str(tries) + " tries to generate Labyrinth", True, (255, 0, 0))
        screen.blit(text, (50, 100))
        pygame.display.flip()

    def cell(self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            return self.grid[x][y]
        else:
            return None

    def reset(self):
        self.grid = [
            [cell(x,y) for y in range(self.rows)]
                for x in range(self.cols)
        ]
    def connect(self, c, direction):
        c.conn[direction] = True
        dx, dy = [(0,-1), (1,0), (0,1), (-1,0)][direction]
        n = self.cell(c.x + dx, c.y + dy)

        if n:
            n.conn[(direction + 2) % 4] = True

    def get_neighbors(self, c):
        dirs = []
        for d, (dx, dy) in enumerate([(0, -1), (1,0), (0,1), (-1,0)]):
            n = self.cell(c.x + dx, c.y + dy)
            if n and not n.filled:
                dirs.append((d, n))
        return dirs

    def grow(self, start, group_id):
        stack = [start]
        start.filled = True
        start.group = group_id

        while stack:
            c = stack.pop()

            neighbors = self.get_neighbors(c)
            random.shuffle(neighbors)

            for d, n in neighbors:
                if not n.filled and random.random() < 0.6:
                    self.connect(c, d)
                    n.filled = True
                    n.group = group_id
                    stack.append(n)

    def generate(self, screen):
        tries = 0
        while True:
            tries += 1
            self.reset()
            self.build_map()

            self.loading_screen(screen, tries)

            if not self.is_fully_connected(self.grid[0][0]):
                continue
            break
        print("Needed " + str(tries) + " tries to generate labyrinth")


    def build_map(self):
        group = 0

        for x in range(self.cols):
            for y in range(self.rows):
                c = self.grid[x][y]

                if not c.filled:
                    self.grow(c, group)
                    group += 1

    def draw(self, screen, size, thickness):
        for x in range(self.cols):
            for y in range(self.rows):
                c = self.grid[x][y]

                px, py = x * size, y * size

                if c.filled:
                    pygame.draw.rect(screen, "black", (px, py, size, size))

                if not c.conn[UP]:
                    pygame.draw.line(screen, "blue", (px, py), (px + size, py), thickness)
                if not c.conn[RIGHT]:
                    pygame.draw.line(screen, "blue", (px + size, py), (px + size, py + size), thickness)
                if not c.conn[DOWN]:
                    pygame.draw.line(screen, "blue", (px, py + size), (px + size, py + size), thickness)
                if not c.conn[LEFT]:
                    pygame.draw.line(screen, "blue", (px, py), (px, py + size), thickness)

    def is_fully_connected(self, start):
        visited = set()
        q = deque([start])

        while q:
            c = q.popleft()
            visited.add((c.x, c.y))

            for d, (dx, dy) in enumerate([(0, -1), (1,0), (0,1), (-1,0)]):
                if c.conn[d]:
                    n = self.cell(c.x + dx, c.y + dy)
                    if n and (n.x, n.y) not in visited:
                        q.append(n)

        for x in range(self.cols):
            for y in range(self.rows):
                c = self.grid[x][y]
                if c.filled and (x, y) not in visited:
                    return False
        return True




