# forSimboloAI
import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Self-Driving Car Track")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Define the car's initial position
car_width = 50
car_height = 100
car_x = display_width // 2 - car_width // 2
car_y = display_height - car_height - 10

clock = pygame.time.Clock()

# Define the game loop
def game_loop():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
# Clear the display
game_display.fill(white)
# Draw the track
pygame.draw.rect(game_display, black, [50, 50, display_width - 100, display_height - 100])
pygame.draw.line(game_display, white, [50, display_height // 2], [display_width - 50, display_height // 2], 5)

# Draw the car
pygame.draw.rect(game_display, green, [car_x, car_y, car_width, car_height])

# Update the display
pygame.display.update()
clock.tick(60)

# Quit the game
pygame.quit()
quit()

# Start the game loop
game_loop()
