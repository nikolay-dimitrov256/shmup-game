# import pygame
# import random
# from app_config import *
from weapons import *

# pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = get_image(0, 0, 192, 192, player_sprite, rotate=90, scale=(80, 80))
        # self.image = pygame.image.load('Graphics/6B.png').convert_alpha()
        # self.image = pygame.transform.scale(self.image, (170 * 0.4, 102 * 0.6))
        self.surf = self.image
        self.rect = self.surf.get_rect(
            center=(
                WIDTH / 2, HEIGHT - 60
            )
        )
        self.lives = 3
        self.current_weapon = PlayerBulletOne
        self.shooting = False
        self.shooting_frames = get_images(0, 0, 4, 192, 192, player_shooting_sprites_2, rotate=90, scale=(80, 80))
        self.animation_counter = 0
        self.animation_index = 0
        self.animation_speed = 2
        self.got_hit = False
        self.destroyed_frames = get_images(0, 0, 21, 192, 192, player_destroyed_sprites, rotate=90, scale=(80, 80))

    def move_player(self, mouse_position):
        self.rect.center = mouse_position

        if self.rect.top < MOVING_AREA_TOP:
            self.rect.top = MOVING_AREA_TOP
        if self.rect.bottom > MOVING_AREA_BOTTOM:
            self.rect.bottom = MOVING_AREA_BOTTOM
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def get_hit(self):
        self.lives -= 1
        self.got_hit = True

        # if self.lives <= 0:
        #     self.kill()

    def animate(self):
        if self.got_hit:
            self.got_hit = self.set_frame(self.destroyed_frames)

            if not self.got_hit:
                if self.lives <= 0:
                    self.kill()

        elif self.shooting:
            self.shooting = self.set_frame(self.shooting_frames)

        else:
            self.surf = self.image

    def set_frame(self, animation_frames: list) -> bool:
        self.surf = animation_frames[self.animation_index]

        self.animation_counter += 1

        if self.animation_counter == self.animation_speed:
            self.animation_index += 1
            self.animation_counter = 0

            if self.animation_index == len(animation_frames):
                self.animation_index = 0
                return False

        return True
