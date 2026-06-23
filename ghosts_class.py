import pygame
import random


class Ghosts:
    def __init__(self, size,hitbox, spawn_point,screenwidth, screenheight, x_cord, y_cord, walls, up_left_score, down_right_score):
        self.active = False
        self.size = size
        self.hitbox = hitbox
        self.spawn_point = spawn_point
        self.direction = 1

        self.percent_up = 0
        self.percent_down = 0
        self.percent_left = 0
        self.percent_right = 0

        self.screenwidth = screenwidth
        self.screenheight = screenheight

        self.cords_center = pygame.Vector2(x_cord, y_cord)
        self.cord_picture = pygame.Vector2(self.cords_center.x + self.size / 2, self.cords_center.y + self.size / 2)
        self.cords_upper_left = pygame.Vector2()
        self.cords_lower_right = pygame.Vector2()

        self.pac_picture = pygame.image.load("pictures/PacMan_open.png")
        self.pac_picture = pygame.transform.scale(self.pac_picture, (size, size))

        self.walls = walls
        self.up_left_score = up_left_score
        self.down_right_score = down_right_score

        self.line = []

    def hitbox(self):
        self.cords_upper_left.x = self.cords_center.x - self.hitbox / 2
        self.cords_upper_left.y = self.cords_center.y - self.hitbox / 2
        self.cords_lower_right.x = self.cords_center.x + self.hitbox / 2
        self.cords_lower_right.y = self.cords_center.y + self.hitbox / 2

    def draw(self, screen, points):
        if (points > self.spawn_point):
            self.active = True
            self.cord_picture = pygame.Vector2(self.cords_center.x - self.size / 2, self.cords_center.y - self.size / 2)
            screen.blit(self.pac_picture, self.cord_picture)
            pygame.draw.circle(screen, "blue", self.cords_center, 5)
            pygame.draw.circle(screen, "green", self.cord_picture, 5)
            for i in self.line:
                t = i
                pygame.draw.circle(screen, "pink", t , 5)

    def move(self, level, cellsize):
        if self.active:
            speed = 10
            if self.is_centered(cellsize):
                self.change_direction(self.direction, level, cellsize)

            if self.direction == 0: # equals up
                self.cords_center.y -= speed
            else:
                if self.direction == 1:  # equals left
                    self.cords_center.x -= speed
                else:
                    if self.direction == 2:  # equals down
                         self.cords_center.y += speed
                    else:
                        if self.direction == 3:  # equals right
                            self.cords_center.x += speed
            self.line.append((self.cords_center.x, self.cords_center.y))

    def change_direction(self, direction, level, cellsize):
        grid_x = int(self.cords_center.x // cellsize)
        grid_y = int(self.cords_center.y // cellsize)
        cell = level.grid[grid_x][grid_y]

        allowed = []
        if cell.conn[0]: allowed.append(0) # Up
        if cell.conn[1]: allowed.append(3) # Right
        if cell.conn[2]: allowed.append(2) # Down
        if cell.conn[3]: allowed.append(1) # Left

        opposite = {0: 2, 3: 1, 2: 0, 1: 3}
        if opposite[self.direction] in allowed and len(allowed) > 1:
            allowed.remove(opposite[self.direction])

        if len(allowed) > 1:
            self.direction = random.choice(allowed)
        else:
            self.direction = allowed[0]

    def is_centered(self, cell_size):
        return (
                abs((self.cords_center.x % cell_size) - cell_size / 2) < 1 and
                abs((self.cords_center.y % cell_size) - cell_size / 2) < 1
        )