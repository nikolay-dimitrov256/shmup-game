import pygame

"""
Player sprites source:
https://craftpix.net/freebies/free-spaceship-pixel-art-sprite-sheets/

Bullets sprites source:
https://bdragon1727.itch.io/fire-pixel-bullet-16x16

Explosions source:
https://bdragon1727.itch.io/retro-impact-effect-pack-all
"""

player_sprite = pygame.image.load('Graphics/Player/Idle.png').convert_alpha()
player_shooting_sprites_1 = pygame.image.load('Graphics/Player/Attack_1.png').convert_alpha()
player_shooting_sprites_2 = pygame.image.load('Graphics/Player/Attack_2.png').convert_alpha()
player_destroyed_sprites = pygame.image.load('Graphics/Player/Destroyed.png').convert_alpha()

enemy1_sprite = pygame.image.load('Graphics/Enemies/1.png').convert_alpha()
enemy1_get_hit_sprite = pygame.image.load('Graphics/Enemies/1_get_hit.png').convert_alpha()

bullet_sheet_00 = pygame.image.load('Graphics/Bullets/All_Fire_Bullet_Pixel_16x16_00.png').convert_alpha()
bullet_sheet_02 = pygame.image.load('Graphics/Bullets/All_Fire_Bullet_Pixel_16x16_02.png').convert_alpha()
bullet_sheet_07 = pygame.image.load('Graphics/Bullets/All_Fire_Bullet_Pixel_16x16_07.png').convert_alpha()

explosions_sheet_01 = pygame.image.load('Graphics/Explosions/Retro Impact Effect Pack 2 A.png').convert_alpha()
