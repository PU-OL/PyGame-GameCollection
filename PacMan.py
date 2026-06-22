import pygame
import random

pygame.init()
pygame.display.set_caption("Pac Man Apples: 0")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0
generator = 0
next_generator = generator
apple_counter = 0
needremove = False

pac_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
pac_picture = pygame.image.load("pictures/PacMan_open.png")
pac_picture = pygame.transform.scale(pac_picture, (40, 40))

ghost_pos = {
    "red": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
    "pink": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
    "blue": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
    "orange": pygame.Vector2(screen.get_width()/2, screen.get_height()/2),
}

apple_pos = {}
apple_del = []

while running:
    generator += 1
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
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

    if(len(apple_pos) < 15 and next_generator < generator):
        next_generator = generator + 100
        new_cord = True
        while(new_cord):
            random_x_pos = random.randint(0,screen.get_width()-5)
            random_y_pos = random.randint(0,screen.get_height()-5)
            if(random_x_pos not in apple_pos):
                new_cord = False

        apple_name = "Apple_" + str(len(apple_pos))
        apple_pos[apple_name] = pygame.Vector2(random_x_pos, random_y_pos)

    screen.blit(pac_picture, pac_pos)

    for i in apple_pos:
        apple_x_reach = apple_pos[i].x - 30
        apple_y_reach = apple_pos[i].y - 30

        apple_x_reach2 = apple_pos[i].x + 30
        apple_y_reach2 = apple_pos[i].y + 30

        if(pac_pos.x > apple_x_reach and pac_pos.x < apple_x_reach2 and pac_pos.y > apple_y_reach and pac_pos.y < apple_y_reach2):
            apple_counter += 1
            pygame.display.set_caption("Pac Man Apples: " + str(apple_counter))
            apple_del.append(i)
            needremove = True

    if(needremove):
        needremove = False
        for i in apple_del:
            del apple_pos[apple_del[0]]
        apple_del.clear()

    for i in apple_pos:
        pygame.draw.circle(screen, "red", apple_pos[i], 5)

    pygame.display.flip()
    dt = clock.tick(60) / 1000.0

pygame.quit()