import pygame
from apples_class import Apple

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

pac_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
pac_picture = pygame.image.load("pictures/PacMan_open.png")
pac_picture = pygame.transform.scale(pac_picture, (40, 40))

ghost_pos = {
    "red": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
    "pink": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
    "blue": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
    "orange": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
}

for i in range(15):
    obj = Apple(apple_id, apple_size)
    apple_id += 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        print("Change to Menu")
    if keys[pygame.K_w]:
        pac_pos.y -= 2
    if keys[pygame.K_s]:
        pac_pos.y += 2
    if keys[pygame.K_a]:
        pac_pos.x -= 2
    if keys[pygame.K_d]:
        pac_pos.x += 2
    if keys[pygame.K_BACKSPACE]:
        pac_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

    screen.fill("black")
    pygame.display.set_caption("Pac Man Apples: " + str(apple_counter))
    screen.blit(pac_picture, pac_pos)
    for i in Apple.iterate_all_instances():
        i.draw(screen)
        if i.ishit(pac_pos):
            apple_counter += 1
            obj = i.objects()
            i.delete()
            del obj

    if Apple.count() < 15:
        obj = Apple(apple_id, apple_size)
        apple_id += 1

    pygame.display.flip()
    dt = clock.tick(60) / 1000.0

pygame.quit()