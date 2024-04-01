import pygame

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

def initialize_game():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('My First Pygame App')

    return screen
