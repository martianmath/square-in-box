import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
window_size = 500  # Size of the window (500x500)
screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Control the Square")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Square settings
square_size = 20
square_x = window_size // 2 - square_size // 2
square_y = window_size // 2 - square_size // 2
speed = 5

# Main game loop
clock = pygame.time.Clock()

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get key states
    keys = pygame.key.get_pressed()

    # Move square based on key press
    if keys[pygame.K_w]:
        square_y -= speed  # Move up
    if keys[pygame.K_s]:
        square_y += speed  # Move down
    if keys[pygame.K_a]:
        square_x -= speed  # Move left
    if keys[pygame.K_d]:
        square_x += speed  # Move right

    # Keep the square inside the grid bounds
    square_x = max(0, min(square_x, window_size - square_size))
    square_y = max(0, min(square_y, window_size - square_size))

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the square
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))

    # Update the screen
    pygame.display.flip()

    # Set the frames per second
    clock.tick(60)
