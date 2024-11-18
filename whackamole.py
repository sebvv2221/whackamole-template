import pygame
import random

def main():
    try:
        pygame.init()
        
        # Constants
        SCREEN_WIDTH = 640
        SCREEN_HEIGHT = 512
        GRID_SIZE = 32
        COLUMNS = SCREEN_WIDTH // GRID_SIZE
        ROWS = SCREEN_HEIGHT // GRID_SIZE
        
        # Initialize screen and mole image
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Whack-a-Mole")
        mole_image = pygame.image.load("mole.png")
        
        # Mole's initial position
        mole_x = 0
        mole_y = 0
        
        # Clock for frame control
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get mouse click position
                    mouse_x, mouse_y = event.pos
                    # Check if the click is within the mole's square
                    if mole_x <= mouse_x < mole_x + GRID_SIZE and mole_y <= mouse_y < mole_y + GRID_SIZE:
                        # Move the mole to a random position
                        mole_x = random.randrange(0, COLUMNS) * GRID_SIZE
                        mole_y = random.randrange(0, ROWS) * GRID_SIZE
            
            # Fill the screen with light green
            screen.fill("light green")
            
            # Draw the grid
            for x in range(0, SCREEN_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, "black", (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, "black", (0, y), (SCREEN_WIDTH, y))
            
            # Draw the mole
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            
            # Update the screen
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
