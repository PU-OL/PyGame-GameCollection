import random
import pygame

class Apple:
    _instances = []

    def __init__(self, id, size, screenwidth, screenheight, walls, score_box_upper_left, score_box_lower_right, room_box_upper_left, room_box_lower_right):
        self.id = id
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.size = size
        self.cords_center = pygame.Vector2()
        self.cords_upper_left = pygame.Vector2()
        self.cords_lower_right = pygame.Vector2()
        self.generate(walls, score_box_upper_left, score_box_lower_right, room_box_upper_left, room_box_lower_right)
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

    def generate(self, walls, score_cords_upper_left, score_cords_lower_right, room_cors_upper_left, room_cors_lower_right):
        used = False
        while not used:
            hit = False
            self.cords_center.x = random.randint(0, self.screenwidth)
            self.cords_center.y = random.randint(0, self.screenheight)
            self.hitbox()
            if not self.border_reached():
                hit = True
            else:
                if self.check_track(walls, score_cords_upper_left, score_cords_lower_right, room_cors_upper_left, room_cors_lower_right):
                    hit = True
                else:
                    for i in Apple.iterate_all_instances():
                        if self.ishit(i.cords_center):
                            hit = True
                            #print("Hit. Generate new cords: ")
            if not hit:
                    used = True

    def hitbox(self):
        hitboxsize = self.size + self.size*3
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

    def check_track(self, walls, up_left_score, down_right_score, up_left_room,down_right_room):
        cx = self.cords_center.x
        cy = self.cords_center.y
        r = self.size

        if up_left_score.x <= cx <= down_right_score.x and \
                up_left_score.y <= cy <= down_right_score.y:
            return True

        if up_left_room.x <= cx <= down_right_room.x and \
                up_left_room.y <= cy <= down_right_room.y:
            return True

        for wall in walls:
            (x1, y1), (x2, y2) = wall
            if y1 == y2:
                if abs(cy - y1) <= r and x1 <= cx <= x2:
                    return True
            if x1 == x2:
                if abs(cx - x1) <= r and y1 <= cy <= y2:
                    return True
        return False

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