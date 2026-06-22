import pygame

pygame.init()
pygame.display.set_caption("Pac Man")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

bloon_pos = pygame.Vector2(screen.get_width(), screen.get_height())
screen.fill("yellow")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, "red", bloon_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_BACKSPACE]:
        screen.fill("black")
    if keys[pygame.K_w]:
        screen.fill("green")


    pygame.display.flip()
    dt = clock.tick(60) / 1000.0
pygame.quit()