import pygame
import sys

# === CLASS === #
from init import initialize_game

screen = initialize_game()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()