import pygame

def show_left_screen(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return 'exit'  # Return to main.py with exit command
            
            # Handle other events, such as button clicks
        
        screen.fill((255, 255, 255))  # Clear the screen or fill with background
        
        # Draw user information
        # For example, draw a rectangle for the profile picture area
        profile_rect = pygame.Rect(50, 50, 100, 100)  # Placeholder dimensions
        pygame.draw.rect(screen, (0, 0, 0), profile_rect, 2)
        
        # Add more drawing code here for nickname, record, etc.
        
        pygame.display.flip()
        
        # For the sake of this example, we'll return to the main menu after one frame
        return 'main_menu_return'
