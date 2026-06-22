import pygame

class PacMan:
    hitbox = 20

    def __init__(self, id, size, x_cord, y_cord, screenwidth, screenheight):
        self.id = id
        self.size = size
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.cords_center = pygame.Vector2(x_cord, y_cord)
        self.cord_picture = pygame.Vector2(self.cords_center.x + self.size / 2, self.cords_center.y + self.size / 2)
        self.cords_upper_left = pygame.Vector2()
        self.cords_lower_right = pygame.Vector2()
        self.pac_hitbox()
        self.pac_picture = pygame.image.load("pictures/PacMan_open.png")
        self.pac_picture = pygame.transform.scale(self.pac_picture, (size, size))


    def draw(self, screen):
        self.cord_picture = pygame.Vector2(self.cords_center.x + self.size / 2, self.cords_center.y + self.size / 2)
        screen.blit(self.pac_picture, self.cord_picture)
        pygame.draw.circle(screen, "blue", self.cords_center, 5)
        pygame.draw.circle(screen, "green", self.cord_picture, 5)

    def collision(self):
        return (
                self.cords_upper_left.x <= 20 or
                self.cords_lower_right.x >= self.screenwidth - 20 or
                self.cords_upper_left.y <= 20 or
                self.cords_lower_right.y >= self.screenheight - 20
        )

    def try_new_collision(self, new_cords):
        cords_upper_left = pygame.Vector2()
        cords_lower_right = pygame.Vector2()

        cords_upper_left.x = new_cords.x - self.hitbox /2
        cords_upper_left.y = new_cords.y - self.hitbox /2
        cords_lower_right.x = new_cords.x + self.hitbox /2
        cords_lower_right.y = new_cords.y + self.hitbox /2

        return (
                cords_upper_left.x <= 20 or
                cords_lower_right.x >= self.screenwidth - 20 or
                cords_upper_left.y <= 20 or
                cords_lower_right.y >= self.screenheight - 20
        )

    def pac_hitbox(self):
        self.cords_upper_left.x = self.cords_center.x - self.hitbox /2
        self.cords_upper_left.y = self.cords_center.y - self.hitbox /2
        self.cords_lower_right.x = self.cords_center.x + self.hitbox /2
        self.cords_lower_right.y = self.cords_center.y + self.hitbox /2

    def move(self, direction):
        new_cords = pygame.Vector2(self.cords_center.x, self.cords_center.y)
        if direction == 0: #equals w
            new_cords.y = self.cords_center.y - 2
        else:
            if direction == 1: #equals a
                new_cords.x = self.cords_center.x - 2
            else:
                if direction == 2: #equals s
                    new_cords.y = self.cords_center.y + 2
                else:
                    if direction == 3: #equals d
                        new_cords.x = self.cords_center.x + 2
        if not self.try_new_collision(new_cords):
            self.cords_center = new_cords