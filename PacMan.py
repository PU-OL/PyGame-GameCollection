import pygame
from pygame.examples import playmus

from apples_class import Apple
from pacman_class import PacMan

pygame.init()
pygame.display.set_caption("Pac Man Apples: 0")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0
apple_id = 0
apple_counter = 0
apple_size = 10
apple_delete = None

def show_border(screenwidth, screenheight):
    pygame.draw.line(screen, "blue", (10, 10), (screenwidth -10, 10), 5)
    pygame.draw.line(screen, "blue", (10, 10), (10, screenheight-10), 5)
    pygame.draw.line(screen, "blue", (10, screenheight-10), (screenwidth-10, screenheight-10), 5)
    pygame.draw.line(screen, "blue", (screenwidth-10, 10), (screenwidth-10, screenheight-10), 5)

ghost_pos = {
    "red": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
    "pink": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
    "blue": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
    "orange": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
}

for i in range(15):
    obj = Apple(apple_id, apple_size, screen.get_width(), screen.get_height())
    apple_id += 1

pacman = PacMan(0,30, 500, 400, screen.get_width(), screen.get_height())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        print("Change to Menu")
    if keys[pygame.K_w]:
        PacMan.move(pacman, 0)
    if keys[pygame.K_a]:
        PacMan.move(pacman, 1)
    if keys[pygame.K_s]:
        PacMan.move(pacman, 2)
    if keys[pygame.K_d]:
        PacMan.move(pacman, 3)
    if keys[pygame.K_BACKSPACE]:
        pacman.cords_center = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

    screen.fill("black")
    pygame.display.set_caption("Pac Man Apples: " + str(apple_counter))
    pacman.draw(screen)
    show_border(screen.get_width(), screen.get_height())
    for i in Apple.iterate_all_instances():
        i.draw(screen)
        if i.ishit(pacman.cords_center):
            apple_counter += 1
            obj = i.objects()
            i.delete()
            del obj

    if Apple.count() < 15:
        obj = Apple(apple_id, apple_size, screen.get_width(), screen.get_height())
        apple_id += 1

    pygame.display.flip()
    dt = clock.tick(60) / 1000.0

pygame.quit()