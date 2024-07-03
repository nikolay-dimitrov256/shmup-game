import pygame

pygame.init()

WIDTH = 700
HEIGHT = 800
MOVING_AREA_TOP = HEIGHT - (HEIGHT // 5)
MOVING_AREA_BOTTOM = HEIGHT
fps = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))