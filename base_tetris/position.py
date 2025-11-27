# so we'll know where to place blocks on the grid
class Position: 
    """
    Class to represent a position in the Tetris grid.
    """
    def __init__(self, row, column):
        self.row = row
        self.column = column
        
