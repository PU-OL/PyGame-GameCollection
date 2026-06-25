import pygame
import random


class Ghosts:
    _instances = []

    def __init__(self, picture, size,hitbox, spawn_point,screenwidth, screenheight, x_cord, y_cord, walls, up_left_score, down_right_score):
        self.active = False
        self.size = size
        self.hitbox = hitbox
        self.spawn_point = spawn_point
        self.direction = 1

        self.screenwidth = screenwidth
        self.screenheight = screenheight

        self.cords_center = pygame.Vector2(x_cord, y_cord)
        self.cord_picture = pygame.Vector2(self.cords_center.x + self.size / 2, self.cords_center.y + self.size / 2)
        self.cords_upper_left = pygame.Vector2()
        self.cords_lower_right = pygame.Vector2()

        ghost_picture = "pictures/" + picture + ".png"
        self.ghost_picture_load = pygame.image.load(ghost_picture)
        self.ghost_picture_load = pygame.transform.scale(self.ghost_picture_load, (size, size))

        self.walls = walls
        self.up_left_score = up_left_score
        self.down_right_score = down_right_score

        self.line = []
        self._instances.append(self)
        self.update_hitbox()

    def delete(self):
        self._instances.remove(self)

    def update_hitbox(self):
        self.cords_upper_left.x = self.cords_center.x - self.hitbox / 2
        self.cords_upper_left.y = self.cords_center.y - self.hitbox / 2
        self.cords_lower_right.x = self.cords_center.x + self.hitbox / 2
        self.cords_lower_right.y = self.cords_center.y + self.hitbox / 2

    def draw(self, screen, points):
        if (points > self.spawn_point):
            self.active = True
            self.cord_picture = pygame.Vector2(self.cords_center.x - self.size / 2, self.cords_center.y - self.size / 2)
            screen.blit(self.ghost_picture_load, self.cord_picture)
            #pygame.draw.circle(screen, "blue", self.cords_center, 5)
            #pygame.draw.circle(screen, "green", self.cord_picture, 5)
            #for i in self.line:
            #    t = i
            #    pygame.draw.circle(screen, "pink", t , 5)

    def move(self, level, cellsize):
        if self.active:
            speed = 2
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
            self.update_hitbox()

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

    def caught_pacman(self, pac_pos):
        return (
                self.cords_upper_left.x <= pac_pos.x <= self.cords_lower_right.x
                and
                self.cords_upper_left.y <= pac_pos.y <= self.cords_lower_right.y
        )

    @classmethod
    def iterate_all_instances(cls):
        return iter(cls._instances)

    @classmethod
    def count(cls):
        return len(cls._instances)