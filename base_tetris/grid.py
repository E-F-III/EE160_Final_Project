import pygame
from .colors import Colors

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
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        #loops through each row
        for row in range(self.num_rows):
            #loops through each column in each row
            for column in range(self.num_cols):
                #prints the column with a space
                print(self.grid[row][column], end = " ")
            #move on to the next line
            print()
    
    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        else:
            return False
    
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0
    
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        #reset
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def draw(self, screen):
        #loops through each row
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # Rect = rectangles, used for positioning, collision detection, drawing objects..
                cell_rect = pygame.Rect(column*self.cell_size + 11, 
                                        row*self.cell_size + 11, self.cell_size -1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)


# import pygame
# from base_tetris.colors import Colors
# #TODO: Create the grid for the game board
# class Grid:
#     def __init__(self):
#         #height of the board
#         self.num_rows = 20
#         #width of the board
#         self.num_cols = 10
#         #size of a block on the board
#         self.cell_size = 30
#         #creates a grid full of 0s for each block in each row and column
#         self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
#         #
#         self.colors = Colors.get_cell_colors()

#     def print_grid(self):
#         #loops through each row
#         for row in range(self.num_rows):
#             #loops through each column in each row
#             for column in range(self.num_cols):
#                 #prints the column with a space
#                 print(self.grid[row][column], end = " ")
#             #move on to the next line
#             print()
    
#     def is_empty(self, row, column):
#         if self.grid[row][column] == 0:
#             return True
#         return False
    
#     def is_row_full(self, row):
#         for column in range(self.num_cols):
#             if self.grid[row][column] == 0:
#                 return False
#             return True
    
#     def clear_row(self, row):
#         for column in range(self.num_cols):
#             self.grid[row][column] = 0
    
#     def move_row_down(self, row, num_rows):
#         for column in range(self.num_cols):
#             self.grid[row+num_rows][column] = self.grid[row][column]
#             self.grid[row][column] = 0

#     def clear_full_rows(self):
#         completed = 0
#         for row in range(self.num_rows-1, 0, -1):
#             if self.is_row_full(row):
#                 self.clear_row(row)
#                 completed += 1

#     def reset(self):
#         #reset
#         self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

#     def draw(self, screen):
#         #loops through each row
#         for row in range(self.num_rows):
#             #loops through each column in each row
#             for column in range(self.num_cols):
#                 cell_value = self.grid[row][column]
#                 cell_rect = pygame.Rect(column*self.cell_size, row*self.cell_size,
#                 self.cell_size, self.cell_size)
#                 pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
            