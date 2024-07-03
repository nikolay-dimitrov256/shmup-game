# import pygame
from abc import ABC, abstractmethod
from app_config import *
from sprite_sheets import *
from helpers import *

# pygame.init()


class Projectile(pygame.sprite.Sprite):
    surf = pygame.Surface((5, 10))
    rect = surf.get_rect()
    direction_x = 0
    direction_y = 0
    frames = []
    animation_index = 0
    animation_counter = 0
    animation_speed = 0

    def __init__(self):
        super().__init__()
        # self.surf = pygame.Surface((5, 10))
        # self.surf.fill('red')
        # self.rect = self.surf.get_rect()
        # self.direction_x = 0
        # self.direction_y = 0
        # self.frames = []
        # self.animation_index = 0
        # self.animation_counter = 0

    def update(self):
        self.rect.move_ip(self.direction_x, self.direction_y)

        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

    def animate(self):
        self.animation_counter += 1
        if self.animation_counter == self.animation_speed:
            self.animation_index += 1
            self.animation_counter = 0

        self.animation_index = self.animation_index % len(self.frames)

        self.surf = self.frames[self.animation_index]

    # @staticmethod
    # def get_images(start_x, start_y, frames, width, height, sprite_sheet: pygame.surface.Surface, rotate=None):
    #     def get_image(posx, posy):
    #         """Extracts image from sprite sheet"""
    #         image = pygame.surface.Surface([width, height])
    #         image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))
    #         image.set_colorkey('black')
    #         if rotate is not None:
    #             image = pygame.transform.rotate(image, rotate)
    #
    #         return image.convert_alpha()
    #
    #     images = []
    #     for col in range(frames):
    #         x = start_x + col * width
    #         y = start_y
    #         current_image = get_image(x, y)
    #         images.append(current_image)
    #
    #     return images


class PlayerProjectile(Projectile):
    def __init__(self, starting_point: tuple):
        super().__init__()
        # self.surf = pygame.Surface((5, 10))
        # self.surf.fill('green')
        # self.rect = self.surf.get_rect(
        #     center=starting_point
        # )
        # self.direction_x, self.direction_y = 0, -20
        # self.damage = 1


class PlayerBulletOne(PlayerProjectile):
    frames = get_images(0, 19 * 16, 5, 16, 16, bullet_sheet_02, rotate=90)

    def __init__(self, starting_point: tuple):
        super().__init__(starting_point)
        self.animation_index = 0
        self.animation_counter = 0
        self.animation_speed = 2
        # self.frames = self.get_images(0, 19 * 16, 5, 16, 16, bullet_sheet_00, rotate=True)
        self.surf = self.frames[self.animation_index]
        self.rect = self.surf.get_rect(center=starting_point)
        self.direction_x, self.direction_y = 0, -10
        self.damage = 1


class EnemyProjectile(Projectile):
    def __init__(self, starting_point: tuple):
        super().__init__()
        self.surf = pygame.Surface((5, 10))
        self.surf.fill('red')
        self.rect = self.surf.get_rect(
            center=starting_point
        )
        self.direction_x, self.direction_y = 0, 2


class EnemyBullet1(EnemyProjectile):
    frames = get_images(31 * 16, 16, 4, 16, 16, bullet_sheet_07)

    def __init__(self, starting_point: tuple):
        super().__init__(starting_point)
        self.animation_index = 0
        self.animation_counter = 0
        self.animation_speed = 2
        self.surf = self.frames[self.animation_index]
        self.rect = self.surf.get_rect(center=starting_point)
        self.direction_x, self.direction_y = 0, 3
