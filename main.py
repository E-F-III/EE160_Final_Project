import pygame, sys
from grid import Grid
from tetrimino import *

pygame.init() 
dark_blue = (44, 44, 127)

# create the surface display (width, height)
screen = pygame.display.set_mode((300, 600)) 
# title it 
pygame.display.set_caption("Python Tetris")
# create clock ( control frame rate; how fast game will run)
clock = pygame.time.Clock()

# create grid :D (20 rows, 10 colums) 
game_grid = Grid()


block = TBlock()



# game loop: event handling, updating positions, drawing objects 

while True:
    for event in pygame.event.get():
        # quit event (exiting out of window)
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 

    # colorsssss (red, green, blue) 
    screen.fill(dark_blue)
    game_grid.draw(screen)
    block.draw(screen)
     # pull up game objects        
    pygame.display.update()
    # tell clock how fast game should run 
    clock.tick(60)


    