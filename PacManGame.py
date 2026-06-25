import pygame
import time

from apples_class import Apple
from ghosts_class import Ghosts
from levelgeneration_class import levelgeneration
from pacman_class import PacMan

class PacManGame:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.name = "Pac-Man"

    def start(self):

        running = True
        main_menu = True
        game = False
        game_over = False
        generated = False
        apple_id = 0
        apple_counter = 0
        apple_size = 10
        apple_delete = None
        apple_max = 0

        pygame.font.init()

        text_start_game = "Press Return to start"
        text_quit_game = "Press + to quit"
        text_game_over = "Game Over"
        font_large = pygame.font.SysFont("Arial", 76, True)
        font_normal_bold = pygame.font.SysFont("Arial", 20, True)
        font_normal = pygame.font.SysFont("Arial", 20)

        def show_border(screenwidth, screenheight):
            pygame.draw.line(self.screen, "pink", (10, 10), (screenwidth - 10, 10), 5)
            pygame.draw.line(self.screen, "pink", (10, 10), (10, screenheight - 10), 5)
            pygame.draw.line(self.screen, "pink", (10, screenheight - 10), (screenwidth - 10, screenheight - 10), 5)
            pygame.draw.line(self.screen, "pink", (screenwidth - 10, 10), (screenwidth - 10, screenheight - 10), 5)

        def func_game_over():
            self.screen.fill("black")

            labyrinth.draw(self.screen, 5)
            pacman.draw(self.screen)
            for ghost in Ghosts.iterate_all_instances():
                ghost.draw(self.screen, apple_counter)
            for apple in Apple.iterate_all_instances():
                apple.draw(self.screen)

            overlay_color = (255, 255, 255, 30)
            overlay_surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
            overlay_surface.fill(overlay_color)
            self.screen.blit(overlay_surface, (0, 0))

            text_game_over_source = font_large.render(text_game_over, True, (255, 0, 0))
            self.screen.blit(text_game_over_source, (self.screen.get_width() / 2 - 200, self.screen.get_height() / 2 - 100))
            text_game_over_apples = "Points: " + str(apple_counter)
            text_game_over_apples = font_normal_bold.render(text_apples, True, (0, 255, 0))
            self.screen.blit(text_game_over_apples, (self.screen.get_width() / 2 - 50, self.screen.get_height() / 2))

            pygame.display.flip()
            time.sleep(5)

        ghost_pos = {
            "red": pygame.Vector2(self.screen.get_width() / 2 + 11, self.screen.get_height() / 2),
            "pink": pygame.Vector2(self.screen.get_width() / 2 + 22, self.screen.get_height() / 2),
            "blue": pygame.Vector2(self.screen.get_width() / 2 + 33, self.screen.get_height() / 2),
            "orange": pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2),
        }

        collums = self.screen.get_width() / 40
        rows = self.screen.get_height() / 40

        point_pos = pygame.Vector2(20, 10)

        labyrinth = None

        apple_max = int((self.screen.get_width() / 150) * (self.screen.get_height() / 150))
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if main_menu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        main_menu = False

                if game_over:
                    generated = False
                    apple_counter = 0
                    del labyrinth
                    del pacman
                    for j in Ghosts.iterate_all_instances():
                        j.delete()
                        del j
                    for j in Apple.iterate_all_instances():
                        j.delete()
                        del j
                    game_over = False

                key = pygame.key.get_pressed()
                if key[pygame.K_PLUS]:
                    running = False
                    main_menu = False
                if key[pygame.K_RETURN]:
                    main_menu = False
                    game = True
                    game_over = False

                    labyrinth = levelgeneration(int(collums), int(rows), 40)
                    point_pos.x = labyrinth.generate(self.screen)
                    point_pos.x = point_pos.x * 43
                    print(point_pos.x + point_pos.y)

                    pacman = PacMan(0, 30, self.screen.get_width() / 2, self.screen.get_height() / 2, self.screen.get_width(),
                                    self.screen.get_height(), labyrinth.walls, labyrinth.score_box_cords_left_up,
                                    labyrinth.score_box_cords_right_down)
                    Ghosts("Geist_Rot", 30, 20, 10, self.screen.get_width(), self.screen.get_height(), self.screen.get_width() / 2,
                           self.screen.get_height() / 2, labyrinth.walls, labyrinth.score_box_cords_left_up,
                           labyrinth.score_box_cords_right_down)
                    Ghosts("Geist_lila", 30, 20, 20, self.screen.get_width(), self.screen.get_height(), self.screen.get_width() / 2,
                           self.screen.get_height() / 2, labyrinth.walls, labyrinth.score_box_cords_left_up,
                           labyrinth.score_box_cords_right_down)
                    Ghosts("Geist_blau", 30, 20, 30, self.screen.get_width(), self.screen.get_height(), self.screen.get_width() / 2,
                           self.screen.get_height() / 2, labyrinth.walls, labyrinth.score_box_cords_left_up,
                           labyrinth.score_box_cords_right_down)
                    Ghosts("Geist_Grün", 30, 20, 40, self.screen.get_width(), self.screen.get_height(), self.screen.get_width() / 2,
                           self.screen.get_height() / 2, labyrinth.walls, labyrinth.score_box_cords_left_up,
                           labyrinth.score_box_cords_right_down)

                self.screen.fill("black")
                text_source = font_normal.render(text_start_game, True, (0, 255, 0))
                self.screen.blit(text_source, (self.screen.get_width() / 2 - 75, self.screen.get_height() / 2 - 36))
                text_source = font_normal.render(text_quit_game, True, (0, 255, 0))
                self.screen.blit(text_source, (self.screen.get_width() / 2 - 50, self.screen.get_height() / 2))
                pygame.display.flip()

            if game:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    print("Change to Menu")
                    game_over = True
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    PacMan.move(pacman, 0)
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    PacMan.move(pacman, 1)
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    PacMan.move(pacman, 2)
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    PacMan.move(pacman, 3)

                if game_over and game == True:
                    func_game_over()
                    main_menu = True
                    game = False
                    continue

                self.screen.fill("black")
                labyrinth.draw(self.screen, 5)
                pacman.draw(self.screen)
                # show_border(screen.get_width(), screen.get_height())

                if apple_counter % 100 == 0 and apple_counter > 99:
                    print("The Ghost come to catch you")

                # print(Apple.count())
                for i in Apple.iterate_all_instances():
                    i.draw(self.screen)
                    if i.ishit(pacman.cords_center):
                        apple_counter += 1
                        obj = i.objects()
                        i.delete()
                        del obj

                text_apples = "Points: " + str(apple_counter)
                text_source = font_normal.render(text_apples, True, (0, 255, 0))
                self.screen.blit(text_source, point_pos)

                if Apple.count() < apple_max:
                    obj = Apple(apple_id, apple_size, self.screen.get_width(), self.screen.get_height(), labyrinth.walls,
                                labyrinth.score_box_cords_left_up, labyrinth.score_box_cords_right_down,
                                labyrinth.room_box_cords_left_up, labyrinth.room_box_cords_right_down)
                    apple_id += 1

                for i in Ghosts.iterate_all_instances():
                    i.move(labyrinth, 40)
                    i.draw(self.screen, apple_counter)
                    if i.active:
                        if i.caught_pacman(pacman.cords_center):
                            print("GAME OVER")
                            game_over = True

                pygame.display.flip()

                self.clock.tick(60) / 1000.0
        return False