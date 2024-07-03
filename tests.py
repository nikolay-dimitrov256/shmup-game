import pygame, os
from typing import List
from collections import deque

pygame.init()

def get_image(posx, posy, width, height, sprite_sheet):
    """Extracts image from sprite sheet"""
    image = pygame.surface.Surface([width, height])
    image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))
    image.set_colorkey('black')

    return image


def animate_sprites(images: deque, x_value, y_value):
    current_image = images[0]
    current_rect = current_image.get_rect(topleft=(x_value, y_value))
    screen.blit(current_image, current_rect)
    images.rotate(-1)


# def get_images(start_x, start_y, frames, width, height, sprite_sheet: pygame.surface.Surface, rotate=False):
#     def get_image(posx, posy, width, height, sprite_sheet):
#         """Extracts image from sprite sheet"""
#         image = pygame.surface.Surface([width, height])
#         image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))
#         image.set_colorkey('black')
#         if rotate:
#             image = pygame.transform.rotate(image, 90)
#
#         return image.convert_alpha()
#
#     images = []
#     for col in range(frames):
#         x = start_x * col
#         y = start_y
#         current_image = get_image(x, y, width, height, sprite_sheet)
#         images.append(current_image)
#
#     return images


screen = pygame.display.set_mode((500, 500))
fps = 30
timer = pygame.time.Clock()

sheet = pygame.image.load('Graphics/Bullets/All_Fire_Bullet_Pixel_16x16_00.png').convert_alpha()
font_location = os.path.join('./', 'ubuntu', 'Ubuntu-R.ttf')
font = pygame.font.Font(font_location, 20)

animations_list = []

# images = get_images(0, 19 * 16, 5, 16, 16, sheet, rotate=True)

for row in range(25):
    animations_list.append([])
    for col in range(5):
        x = col * 16
        y = row * 16
        image = get_image(x, y, 16, 16, sheet)

        animations_list[row].append(image)

    animations_list[row] = deque(animations_list[row])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((50, 50, 50))

    for row in range(len(animations_list)):
        y = row * 16
        x = 0
        animate_sprites(animations_list[row], x, y)

    pygame.display.flip()
    timer.tick(fps)

pygame.quit()