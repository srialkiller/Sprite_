import os
import sys
import pygame

from .settings import *
from .player import Player


class Game:
    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.running = True
        self.clock = pygame.time.Clock()

        self.dir = os.path.dirname(__file__)
        self.dir_images = os.path.join(self.dir, '../img')

    def start(self):
        self.new()
        self.run()

    def new(self):
        self.generate_elements()
        self.run()

    def generate_elements(self):
        self.player = Player(self.dir_images)

        self.sprites = pygame.sprite.Group()

        self.sprites.add(self.player)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()

    def quit(self):
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
            self.player.handle_event(event)

    def draw(self):
        self.surface.fill(BGCOLOR)
        self.sprites.draw(self.surface)

    def update(self):
        pygame.display.flip()  # actualizar pantalla

    def stop(self):
        pass
