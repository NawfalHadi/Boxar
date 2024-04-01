import pygame
import sys

# === CLASS === #
import init
from init import initialize_game

# DEFINE VARIABLE
LEFT_PANEL_WIDTH = int(init.SCREEN_WIDTH * 35 / 100)
RIGHT_PANEL_WIDTH = int(init.SCREEN_HEIGHT * 65 / 100)
PANEL_HEIGHT = init.SCREEN_HEIGHT

screen = initialize_game()

def left_panel():
    pygame.draw.rect(screen, (255, 255, 255), (LEFT_PANEL_WIDTH // 6 + 1, PANEL_HEIGHT // 6 + 1, LEFT_PANEL_WIDTH // 1.5 - 2, PANEL_HEIGHT // 1.5 - 2))
    pygame.draw.rect(screen, (0, 0, 0), (LEFT_PANEL_WIDTH // 6, PANEL_HEIGHT // 6, LEFT_PANEL_WIDTH // 1.5, PANEL_HEIGHT // 1.5), 5)  # Border

def right_panel():
    pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Panel Drawwing
    pygame.draw.rect(screen, (255,255,255), (0, 0, LEFT_PANEL_WIDTH, init.SCREEN_HEIGHT))
    left_panel()
    
    pygame.draw.rect(screen, (255,255,255), (LEFT_PANEL_WIDTH, 0, RIGHT_PANEL_WIDTH, init.SCREEN_HEIGHT))
    right_panel()

    pygame.display.flip()