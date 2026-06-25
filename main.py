import pygame
import PacManGame

pygame.init()
pygame.display.set_caption("Games")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
games = []

pacman = PacManGame.PacManGame(screen, clock)
games.append(pacman)

text_quit_game = "Press ESCAPE to quit"
font_large = pygame.font.SysFont("Arial", 76, True)
font_normal_bold = pygame.font.SysFont("Arial", 20, True)
font_normal = pygame.font.SysFont("Arial", 20)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Key = pygame.key.get_pressed()
    if Key[pygame.K_1]:
        pacman.start()
    if Key[pygame.K_ESCAPE]:
        running = False

    screen.fill("black")

    count = 1
    for i in games:
        text_source = font_normal.render("Press " + str(count) + " to start " + str(i.name), True, (0, 255, 0))
        screen.blit(text_source, (screen.get_width() / 2 - 75, (screen.get_height() / 2 + count*10)))
        count += 1

    text_source = font_normal.render(text_quit_game, True, (0, 255, 0))
    screen.blit(text_source, (screen.get_width() / 2 - 75, screen.get_height() / 2 - count*10))
    pygame.display.flip()
