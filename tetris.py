import pygame, sys
import random

from grid import Grid

pygame.init()
dark_blue = (44, 44, 127) # rgb

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game_grid = Grid()
game_grid.print_grid()

while True:

    for event in pygame.event.get():
        # Game loop stopper
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(dark_blue)

    pygame.display.update()
    clock.tick(60) # game speed. can change this for difficulty
