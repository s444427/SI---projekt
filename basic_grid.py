# Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# Grid size
GSIZE = 20

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 35
HEIGHT = 35

# This sets the margin between each cell
MARGIN = 5

# Window size
SCREEN_WIDTH = GSIZE * (WIDTH + MARGIN) + MARGIN 
SCREEN_HEIGHT = GSIZE * (HEIGHT + MARGIN) + MARGIN

# Set some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (140, 95, 65)
DBROWN = (65, 50, 20)

# Define a Tractor object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'tractor'
class Tractor(pygame.sprite.Sprite):
    def __init__(self):
        super(Tractor, self).__init__()
        self.surf = pygame.Surface((WIDTH, HEIGHT))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(topleft=(MARGIN, MARGIN))

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -(HEIGHT + MARGIN))
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, HEIGHT + MARGIN)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-(WIDTH + MARGIN), 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(WIDTH + MARGIN, 0)

        if self.rect.left < MARGIN:
            self.rect.left = MARGIN
        if self.rect.right > SCREEN_WIDTH-MARGIN:
            self.rect.right = SCREEN_WIDTH-MARGIN
        if self.rect.top <= MARGIN:
            self.rect.top = MARGIN
        if self.rect.bottom >= SCREEN_HEIGHT-MARGIN:
            self.rect.bottom = SCREEN_HEIGHT-MARGIN
# Name the window
pygame.display.set_caption("Inteligentny Traktor")

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate tractor. Right now, this is just a rectangle.
tractor = Tractor()

# Variable to keep the main loop running
running = True

clock = pygame.time.Clock()

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    # Set the screen background
    tractor.update(pressed_keys)

    screen.fill(DBROWN)
    
    for row in range(GSIZE):
        for column in range(GSIZE):
            color = BROWN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Draw the player on the screen
    screen.blit(tractor.surf, tractor.rect)

    # Update the screen                          
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(10)
