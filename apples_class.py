import random
import pygame
from PacMan import screen

class Apple:
    _instances = []
    hitboxsize = 20

    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.cords_center = pygame.Vector2()
        self.cords_upper_left = pygame.Vector2()
        self.cords_lower_right = pygame.Vector2()
        self.generate()
        self._instances.append(self)
        #print("Instance created. id: ", self.id)

    def objects(self):
        return self

    def delete(self):
        self._instances.remove(self)
        print("Instance deleted. id: " + str(self.id))

    def draw(self):
        pygame.draw.circle(screen, "red", self.cords_center, self.size)

    def generate(self):
        used = False
        while not used:
            hit = False
            self.cords_center.x = random.randint(0, screen.screenwidth)
            self.cords_center.y = random.randint(0, screen.screenheight)
            self.hitbox()
            for i in Apple.iterate_all_instances():
                if self.ishit(i.cords_center) and self.border_reached():
                    hit = True
                    #print("Hit. Generate new cords: ")
            if not hit:
                    used = True

    def hitbox(self):
        self.cords_upper_left.x = self.cords_center.x - self.hitboxsize /2
        self.cords_upper_left.y = self.cords_center.y - self.hitboxsize /2
        self.cords_lower_right.x = self.cords_center.x + self.hitboxsize /2
        self.cords_lower_right.y = self.cords_center.y + self.hitboxsize /2

    def ishit(self, collision_position):
        return (
                self.cords_upper_left.x <= collision_position.x <= self.cords_lower_right.x
                and
                self.cords_upper_left.y <= collision_position.y <= self.cords_lower_right.y
        )

    def border_reached(self):
        return (
                self.cords_upper_left.x <= 20 or
                self.cords_lower_right.x >= screen.screenwidth - 20 or
                self.cords_upper_left.y <= 20 or
                self.cords_lower_right.y >= screen.screenheight - 20
        )

    @classmethod
    def iterate_all_instances(cls):
        return iter(cls._instances)

    @classmethod
    def count(cls):
        return len(cls._instances)