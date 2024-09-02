import pygame
import os

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 600, 600

# Set up display
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)  # Use SRCALPHA for per-pixel alpha

pygame.display.set_caption("My PNG-Tuber")

# Load images
images_folder = 'resources\profile\images'
default_image = pygame.image.load(os.path.join(images_folder, '1.png')).convert_alpha()
happy_image = pygame.image.load(os.path.join(images_folder, '2.png')).convert_alpha()
sad_image = pygame.image.load(os.path.join(images_folder, '3.png')).convert_alpha()
bronya = pygame.image.load(os.path.join(images_folder, '4.png')).convert_alpha()

# Scale images to fit window
default_image = pygame.transform.scale(default_image, (WIDTH, HEIGHT))
happy_image = pygame.transform.scale(happy_image, (WIDTH, HEIGHT))
sad_image = pygame.transform.scale(sad_image, (WIDTH, HEIGHT))
bronya = pygame.transform.scale(bronya, (WIDTH, HEIGHT))

# Set initial image
current_image = default_image

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # Key '1' to show default image
                current_image = default_image
            elif event.key == pygame.K_2:  # Key '2' to show happy image
                current_image = happy_image
            elif event.key == pygame.K_3:  # Key '3' to show sad image
                current_image = sad_image
            elif event.key == pygame.K_4:  # Key '3' to show sad image
                current_image = bronya

    # Clear screen
    win.fill((0, 0, 0, 0))
    
    # Draw the current image
    win.blit(current_image, (0, 0))
    
    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
