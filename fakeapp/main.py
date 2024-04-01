import pygame
import sys
from left_screen import show_left_screen
from right_screen import show_right_screen
from scenes.play_vs_bot import show_play_vs_bot
from scenes.shadow_boxing import show_shadow_boxing
from scenes.pad_works import show_pad_works
from scenes.tutorial import show_tutorial

def main_menu(screen):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    # Define button areas (for simplicity, using rectangles)
    play_vs_bot_button = pygame.Rect(450, 100, 250, 50)
    shadow_boxing_button = pygame.Rect(450, 200, 250, 50)
    pad_works_button = pygame.Rect(450, 275, 250, 50)
    tutorial_button = pygame.Rect(450, 350, 250, 50)
    exit_button = pygame.Rect(650, 530, 100, 40)

    font = pygame.font.Font(None, 32)
    
    # Main menu loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_vs_bot_button.collidepoint(event.pos):
                    return 'play_vs_bot'
                elif shadow_boxing_button.collidepoint(event.pos):
                    return 'shadow_boxing'
                elif pad_works_button.collidepoint(event.pos):
                    return 'pad_works'
                elif tutorial_button.collidepoint(event.pos):
                    return 'tutorial'
                elif exit_button.collidepoint(event.pos):
                    return 'quit'

        # Drawing the menu (you would replace this with actual drawing code)
        screen.fill((255, 255, 255))  # Fill screen with white
        pygame.draw.rect(screen, (0, 0, 0), play_vs_bot_button)
        pygame.draw.rect(screen, (0, 0, 0), shadow_boxing_button)
        pygame.draw.rect(screen, (0, 0, 0), pad_works_button)
        pygame.draw.rect(screen, (0, 0, 0), tutorial_button)
        pygame.draw.rect(screen, (0, 0, 0), exit_button)

        pygame.display.flip()

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Main Menu")

# Main loop
current_screen = 'main_menu'

while current_screen != 'quit':
    if current_screen == 'main_menu':
        current_screen = main_menu(screen)
    elif current_screen == 'left_screen':
        current_screen = show_left_screen(screen)
    elif current_screen == 'right_screen':
        current_screen = show_right_screen(screen)
    elif current_screen == 'play_vs_bot':
        current_screen = show_play_vs_bot(screen)
    elif current_screen == 'shadow_boxing':
        current_screen = show_shadow_boxing(screen)
    elif current_screen == 'pad_works':
        current_screen = show_pad_works(screen)
    elif current_screen == 'tutorial':
        current_screen = show_tutorial(screen)
    # Handle returning to the main menu or exiting
    if current_screen == 'main_menu_return':
        current_screen = 'main_menu'
    elif current_screen == 'exit':
        break

# Clean up and quit
pygame.quit()
sys.exit()
