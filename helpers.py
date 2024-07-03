import pygame


def get_image(posx, posy, width, height, sprite_sheet: pygame.surface.Surface, rotate=None, scale=None):
    """Extracts image from sprite sheet"""
    image = pygame.surface.Surface([width, height])
    image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))
    image.set_colorkey('black')
    if rotate is not None:
        image = pygame.transform.rotate(image, rotate)

    if scale is not None:
        x_scale, y_scale = scale
        image = pygame.transform.scale(image, (x_scale, y_scale))

    return image.convert_alpha()


def get_images(start_x, start_y, frames, width, height, sprite_sheet: pygame.surface.Surface, rotate=None, scale=None):
    # def get_image(posx, posy):
    #     """Extracts image from sprite sheet"""
    #     image = pygame.surface.Surface([width, height])
    #     image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))
    #     image.set_colorkey('black')
    #     if rotate is not None:
    #         image = pygame.transform.rotate(image, rotate)
    #
    #     if scale is not None:
    #         x_scale, y_scale = scale
    #         image = pygame.transform.scale(image, (x_scale, y_scale))
    #
    #     return image.convert_alpha()

    images = []
    for col in range(frames):
        x = start_x + col * width
        y = start_y
        current_image = get_image(x, y, width, height, sprite_sheet, rotate, scale)
        images.append(current_image)

    return images
