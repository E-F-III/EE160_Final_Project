from .grid import Grid
from .tetrimino import *
import random

class Game:
    """
    Base Tetris game class, handles the game logic and state.
    """
    def __init__(self):
        """
        Initialize the game with a grid and a set of tetrimino blocks.
        """
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.fall_speed = 500
        self.fall_time = 0
    
    def update_score(self, lines_cleared, move_down_points):
        """
        Update the score based on the number of lines cleared and points for moving down.
        """
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 800
        elif lines_cleared > 4:
            self.score += 1600
        self.score += move_down_points

    def get_random_block(self):
        """
        Get a random tetrimino block from the available blocks.
        """
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        """
        Move the current block left, if possible.
        """
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,1)

    def move_right(self):
        """
        Move the current block right, if possible.
        """
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,-1)
    
    def move_down(self):
        """
        Move the current block down, if possible.
        """
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1,0)
            self.lock_block()
            return False
        return True
    
    def instant_drop(self):
        not_locked = True
        while not_locked:
            not_locked = self.move_down()
            self.update_score(0, 1)
    
    def lock_block(self):
        """
        Lock the current block in place and update the game state.
        """
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        
        self.update_score(rows_cleared, 0)
        
        if hasattr(self, 'add_lines'):
            self.add_lines(rows_cleared)

        if self.block_fits() == False:
            self.game_over = True
    
    def reset(self):
        """
        Reset the game state, including the grid, blocks, current and next blocks, and score.
        """
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        """
        Check if the current block fits in the grid without overlapping existing blocks.
        """
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        """
        Rotate the current block, if possible.
        """
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
    
    def rotate_counterclockwise(self):
        self.current_block.undo_rotation()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.rotate()
    
    def block_inside(self): #boundary check
        """
        Check if the current block is inside the grid boundaries.
        """
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        
        return True
    
    def draw(self, screen):
        """
        Draw the game state on the screen.
        """
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)