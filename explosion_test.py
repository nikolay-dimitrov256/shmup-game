import pygame


def get_images(start_x, start_y, frames, width, height, sprite_sheet: pygame.surface.Surface, rotate=None):
    def get_image(posx, posy):
        """Extracts image from sprite sheet"""
        image = pygame.surface.Surface([width, height])
        image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))
        image.set_colorkey('black')
        if rotate is not None:
            image = pygame.transform.rotate(image, rotate)

        return image.convert_alpha()

    images = []
    for col in range(frames):
        x = start_x + col * width
        y = start_y
        current_image = get_image(x, y)
        images.append(current_image)

    return images


pygame.init()

screen = pygame.display.set_mode((400, 400))
fps = 1
timer = pygame.time.Clock()
index = 0
counter = 0

explosions_sheet_01 = pygame.image.load('Graphics/Explosions/Retro Impact Effect Pack 2 A.png').convert_alpha()
images = get_images(8, 97 * 8, 4, 8*8, 6*8, explosions_sheet_01)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill('black')

    image = images[index]
    rect = image.get_rect(topleft=(5, 5))
    index += 1
    if index == len(images):
        index = 0

    screen.blit(image, rect)

    pygame.display.flip()
    timer.tick(fps)

pygame.quit()
