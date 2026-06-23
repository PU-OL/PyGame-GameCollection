import random
import pygame

class Apple:
    _instances = []

    def __init__(self, id, size, screenwidth, screenheight):
        self.id = id
        self.screenwidth = screenwidth
        self.screenheight = screenheight
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
        #print("Instance deleted. id: " + str(self.id))

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.cords_center, self.size)
        pygame.draw.circle(screen, "blue", self.cords_center, 3)

    def generate(self):
        used = False
        while not used:
            hit = False
            self.cords_center.x = random.randint(0, self.screenwidth)
            self.cords_center.y = random.randint(0, self.screenheight)
            self.hitbox()
            if not self.border_reached():
                hit = True
            else:
                for i in Apple.iterate_all_instances():
                    if self.ishit(i.cords_center):
                        hit = True
                        #print("Hit. Generate new cords: ")
            if not hit:
                    used = True

    def hitbox(self):
        hitboxsize = self.size + self.size*2.5
        self.cords_upper_left.x = self.cords_center.x - hitboxsize /2
        self.cords_upper_left.y = self.cords_center.y - hitboxsize /2
        self.cords_lower_right.x = self.cords_center.x + hitboxsize /2
        self.cords_lower_right.y = self.cords_center.y + hitboxsize /2

    def ishit(self, collision_position):
        return (
                self.cords_upper_left.x <= collision_position.x <= self.cords_lower_right.x
                and
                self.cords_upper_left.y <= collision_position.y <= self.cords_lower_right.y
        )

    def border_reached(self):
        return (
                self.cords_upper_left.x >= 10 and
                self.cords_lower_right.x <= self.screenwidth - 10 and
                self.cords_upper_left.y >= 10 and
                self.cords_lower_right.y <= self.screenheight - 10
        )

    @classmethod
    def iterate_all_instances(cls):
        return iter(cls._instances)

    @classmethod
    def count(cls):
        return len(cls._instances)