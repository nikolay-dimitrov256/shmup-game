# import pygame
import random

import pygame.image

# from app_config import *
from weapons import *
from sprite_sheets import *

# pygame.init()


class Enemy(pygame.sprite.Sprite):
    enemies_killed = 0
    image = None
    get_hit_image = None
    dead = False
    explosion_images = []
    explosion_index = 0
    explosion_speed = 1
    explosion_counter = 0

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 40))
        self.surf.fill('purple')
        self.rect = self.surf.get_rect(
            center=(
                random.choice([0, WIDTH]), random.randint(20, 500)
            )
        )
        self.starting_x = self.rect.center[0]
        self.speed = 3
        self.direction_x = self.speed if self.starting_x < WIDTH else -self.speed
        self.direction_y = 0
        self.turned = False
        self.health = 1
        self.got_hit_counter = 0
        self.bullet = EnemyProjectile

    def update(self):
        if self.dead:
            return None

        if not self.turned and self.rect.center[0] not in range(WIDTH + 1):
            self.direction_x = -self.direction_x
            self.turned = True

        elif self.turned and self.rect.center[0] in range(WIDTH + 1):
            self.turned = False

        self.rect.move_ip(self.direction_x, self.direction_y)

    def get_hit(self, damage):

        self.health -= damage
        self.got_hit_counter = 10

        if self.health < 1:
            self.dead = True
            Enemy.enemies_killed += 1
            # self.kill()

    def animate(self):
        if self.dead:
            self.surf = self.explosion_images[self.explosion_index]
            self.explosion_counter += 1
            if self.explosion_counter == self.explosion_speed:
                self.explosion_index += 1
                self.explosion_counter = 0
                if self.explosion_index == len(self.explosion_images):
                    self.kill()

        elif self.got_hit_counter > 0:
            self.surf = self.get_hit_image
            self.got_hit_counter -= 1
        else:
            self.surf = self.image

    @property
    def shoot(self) -> bool:

        return random.choice([True] + [False] * 100)


class Enemy1(Enemy):
    image = enemy1_sprite
    image = pygame.transform.scale(image, (124 * 0.5, 135 * 0.5))
    image = pygame.transform.rotate(image, 180)
    get_hit_image = enemy1_get_hit_sprite
    get_hit_image = pygame.transform.scale(get_hit_image, (124 * 0.5, 135 * 0.5))
    get_hit_image = pygame.transform.rotate(get_hit_image, 180)
    explosion_images = get_images(8, 97 * 8, 4, 8*8, 6*8, explosions_sheet_01, scale=(90, 70))

    def __init__(self):
        super().__init__()
        self.surf = self.image
        self.rect = self.surf.get_rect(
            center=(random.choice([0, WIDTH]), random.randint(40, 500))
        )
        self.starting_x = self.rect.center[0]
        self.speed = 3
        self.direction_x = self.speed if self.starting_x < WIDTH else -self.speed
        self.direction_y = 0
        self.turned = False
        self.health = 2
        self.got_hit_counter = 0
        self.dead = False
        self.explosion_index = 0
        self.explosion_counter = 0
        self.explosion_speed = 5
        self.bullet = EnemyBullet1
