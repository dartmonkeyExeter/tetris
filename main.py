grid = []
import os, time, keyboard
clear = lambda: os.system('cls')

class piece:
    def __init__(self, shape):
        self.shape = shape
        self.rotation = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4

    def get_current_shape(self):
        return self.shape[self.rotation]

class squarePiece(piece):
    def __init__(self):
        shape = [
            "**",
            "**"
        ]
        super().__init__(shape)

for i in range(0, 160):
    grid.append("-")

def display_grid():
    for i in range(0, 160, 10):
        try:
            print(grid[i], grid[i+1], grid[i+2], grid[i+3], grid[i+4], grid[i+5], grid[i+6], grid[i+7], grid[i+8], grid[i+9])
        except IndexError:
            break

def update_grid():
    grid[4,5] = squarePiece(piece).shape
clear()
while True:
    update_grid()
    display_grid()


    
    
    
