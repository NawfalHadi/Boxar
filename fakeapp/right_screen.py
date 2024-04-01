import pygame

def show_right_screen(screen):
    running = True
    # Define buttons
    play_vs_bot_button = pygame.Rect(450, 100, 250, 50)
    # ...define other buttons similarly
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return 'exit'  # Return to main.py with exit command
            
            # Handle button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_vs_bot_button.collidepoint(event.pos):
                    # Here, return to main.py to change the screen
                    return 'play_vs_bot'
                # Handle other buttons similarly
        
        screen.fill((255, 255, 255))  # Clear the screen or fill with background
        
        # Draw buttons and text
        pygame.draw.rect(screen, (200, 200, 200), play_vs_bot_button)
        # ...draw other buttons similarly
        
        # Draw the text for each button
        font = pygame.font.SysFont(None, 36)
        text_surf = font.render('PLAY VS BOT', True, (0, 0, 0))
        screen.blit(text_surf, (play_vs_bot_button.x + 20, play_vs_bot_button.y + 10))
        # ...render and blit other texts similarly
        
        pygame.display.flip()
        
        # For the sake of this example, we'll return to the main menu after one frame
        return 'main_menu_return'
