import pygame 
from .colors import Colors 
from .position import Position

class Block:
    def __init__(self, id):
        self.id = id # to differentiate the blocks
        self.cells = {} # a dictionary that will hold the diff rotation states of the block; each state will be a list of tile coordinates that will make blocks shape 
        self.cell_size = 30 # each tile is 30 pixls wide and 30 pixels high 

        '''
          tracks current position of block on the grid  
          '''
        self.row_offset = 0 # how many rows down the block is
        self.column_offset = 0 # how many columns to the right the block is
        

        self.rotation_state = 0 # which rotation state the block is in

        # get colors from Colors class
        self.colors = Colors.get_cell_colors()

        # color of each tile in the block
        self.tile_colors = []
        
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state] # retrieves the tile coordinates for the current rotation state
        moved_tiles = [] # need a list bc each block consists of multiple tiles, need all tiles in one place together to make a block move 
        # convert shape coordinates to grid coordinates
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
            
        return moved_tiles
    
    def rotate(self):
        self.rotation_state += 1 
        if self.rotation_state == len(self.cells): # if rotation state exceeds available states, loop back to 0
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1: # if rotation state goes below 0, loop back to last state
            self.rotation_state = len(self.cells) - 1

# draws the block on the screen
    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions() #  get the current tile positions of the block
        for tile in tiles: 
            # draw each tile as a rectangle
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
                                    offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1) 
            # draw tile with block's color
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
 