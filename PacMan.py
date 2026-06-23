import pygame

from apples_class import Apple
from levelgeneration_class import levelgeneration
from pacman_class import PacMan

pygame.init()
pygame.display.set_caption("Pac Man")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
generated = False
dt = 0
apple_id = 0
apple_counter = 0
apple_size = 10
apple_delete = None
apple_max = 0

pygame.font.init()

text_loading = "Labyrinth gets generated. Please wait..."
font_large = pygame.font.SysFont("Arial", 36)
font_normal = pygame.font.SysFont("Arial", 20)

def show_border(screenwidth, screenheight):
    pygame.draw.line(screen, "pink", (10, 10), (screenwidth -10, 10), 5)
    pygame.draw.line(screen, "pink", (10, 10), (10, screenheight-10), 5)
    pygame.draw.line(screen, "pink", (10, screenheight-10), (screenwidth-10, screenheight-10), 5)
    pygame.draw.line(screen, "pink", (screenwidth-10, 10), (screenwidth-10, screenheight-10), 5)

ghost_pos = {
    "red": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
    "pink": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
    "blue": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
    "orange": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
}

collums = screen.get_width()/40
rows = screen.get_height()/40

point_pos = pygame.Vector2(20,10)

labyrinth = levelgeneration(int(collums), int(rows))
point_pos.x = labyrinth.generate(screen)
point_pos.x = point_pos.x * 43
print(point_pos.x + point_pos.y)

apple_max = int((screen.get_width()/150)* (screen.get_height()/150))
print("Max apples: " + str(apple_max))

pacman = PacMan(0,30, screen.get_width()/2, screen.get_height()/2, screen.get_width(), screen.get_height())

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
    labyrinth.draw(screen, 40, 5)
    pacman.draw(screen)
    #show_border(screen.get_width(), screen.get_height())

    for i in Apple.iterate_all_instances():
        i.draw(screen)
        if i.ishit(pacman.cords_center):
            apple_counter += 1
            obj = i.objects()
            i.delete()
            del obj

    text_apples = "Points: " + str(apple_counter)
    text_source = font_normal.render(text_apples, True, (0, 255, 0))
    screen.blit(text_source, point_pos)

    if Apple.count() < apple_max:
        obj = Apple(apple_id, apple_size, screen.get_width(), screen.get_height())
        apple_id += 1

    pygame.display.flip()
    dt = clock.tick(60) / 1000.0

pygame.quit()