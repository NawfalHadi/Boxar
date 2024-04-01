import pygame

def show_shadow_boxing(screen):
    # Clear the screen
    screen.fill((255, 255, 255))

    # Game logic and drawing for "Shadow Boxing" screen goes here

    # Placeholder text
    font = pygame.font.SysFont('Arial', 24)
    text_surface = font.render('Shadow Boxing Screen', True, (0, 0, 0))
    screen.blit(text_surface, (100, 100))

    # Keep updating the display as long as this screen is active
    pygame.display.flip()

    # Wait for an event (for example, button to go back)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                return 'main_menu_return'
