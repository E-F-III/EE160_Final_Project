class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {} 
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = []
    
    def draw(self, screen):
        '''
        draw the block on the screen
        '''