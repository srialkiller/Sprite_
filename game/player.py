import os

import pygame
from .settings import *


class Player(pygame.sprite.Sprite):

    def __init__(self, dir_images):
        pygame. sprite.Sprite.__init__(self)

        self.sheet = pygame.image.load(os.path.join(dir_images, 'player.png'))
        self.sheet.set_clip(pygame.Rect(57, 137, 30, 52))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.frame = 0
        self.left_states = {0: (60, 205, 24, 50), 1: (11, 207, 25, 49), 2: (108, 206, 26, 50)}
        self.right_states = {0: (60, 77, 24, 50), 1: (10, 78, 26, 50), 2: (108, 79, 25, 49)}
        self.up_states = {0: (57, 13, 30, 48), 1: (10, 15, 29, 49), 2: (105, 15, 29, 49)}
        self.down_states = {0: (57, 137, 30, 52), 1: (9, 139, 29, 52), 2: (106, 139, 29, 52)}

        self.playing = True

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 5

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
