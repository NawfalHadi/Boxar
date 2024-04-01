import pygame

def initialize_game():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('My First Pygame App')

    return screen
