import sys
import pygame
import random

from scripts.entities import PhysicsEntity
from scripts.drop import Drop
from scripts.utils import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Coolect")

        self.screen = pygame.display.set_mode((800, 600))
        self.display = pygame.Surface((400, 300))

        self.clock = pygame.time.Clock()

        self.bg_color = (14, 150, 170)

        self.assets = {
            'penguin' : load_image('entities/penguin/licensed/penguin3.jpg', (157, 145, 255, 255)),
            'drop' : load_image('entities/drop.png', (255, 255, 255))
        }

        self.movement = [False, False]
        self.penguin = PhysicsEntity(self, 'penguin', (40, 40), (195, 250))

        self.drops = []

        self.score = 0

    def run(self):
        while True:
            self.display.fill(self.bg_color)

            # update penguin position and render
            self.penguin.update_pos(((self.movement[1]-self.movement[0])*3, 0))
            self.penguin.render(self.display)

            # update drop positions and render
            for drop in self.drops:
                if drop.check_collision(pygame.Rect(*self.penguin.pos, *self.penguin.size)):
                    self.score+=1
                    self.drops.remove(drop)
                if drop.check_boundary():
                    self.drops.remove(drop)
                else:
                    drop.update_pos()
                    drop.render(self.display)

            # add new drops
            if random.random() < 0.01:
                self.drops.append(Drop(self, 'drop', (15, 20), (random.randrange(20, 370), 15)))

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False

            # final render
            self.screen.blit((pygame.transform.scale(self.display, self.screen.get_size())), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()