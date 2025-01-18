#import displayio
#from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
#import time
#from adafruit_display_text import label
#import random


import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_size = (128, 128)
screen = pygame.display.set_mode(window_size)


pygame.display.set_caption("Oscar")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((0, 0, 0))  # Fill with black

    # Update the display
    pygame.display.flip()


pygame.quit()
sys.exit()