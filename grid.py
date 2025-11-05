import pygame
from colors import Colors
#TODO: Create the grid for the game board
class Grid:
    def __init__(self):
        #height of the board
        self.num_rows = 20
        #width of the board
        self.num_cols = 10
        #size of a block on the board
        self.cell_size = 30
        #creates a grid full of 0s for each block in each row and column
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        #
        self.colors = self.get_cell_colors()



    def print_grid(self):
        #loops through each row
        for row in range(self.num_rows):
            #loops through each column in each row
            for column in range(self.num_cols):
                #prints the column with a space
                print(self.grid[row][column], end = " ")
            #move on to the next line
            print()
    
    def is_empty(self, row, column):
        pass
    
    def is_row_full(self, row):
        pass
    
    def clear_row(self, row):
        pass
    
    def move_row_down(self, row, num_rows):
        pass

    def clear_full_rows(self):
        pass

    def reset(self):
        #reset
        self.grid.reset()

    def draw(self, screen):
        #loops through each row
        for row in range(self.num_rows):
            #loops through each column in each row
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size, row*self.cell_size,
                self.cell_size, self.cell_size)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
            