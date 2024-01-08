import pygame
import numpy as np

pygame.display.init()

pygame.display.set_caption("Tetris")
window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

class tetronimo:
    def __init__(self, x, y, color, shape):
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.rotation = 0
    def move_down(self):
        self.y += 1
    
    def move_left(self):    
        if self.x > 0 :
            self.x -= 1
    
    def move_right(self):
        if self.x < 10 - len(self.shape[0]):
            self.x += 1
    def rotate_clockwise(self):
        self.shape = np.rot90(self.shape, k=-1)
        self.rotation = (self.rotation - 1) % 4
        
            

grid = np.zeros((20, 10))

line_piece = [
    [1],
    [1],
    [1],
    [1]
]

t_piece = [
    [1, 1, 1],
    [0, 1, 0]
]

current_piece = tetronimo(5, 0, (255, 0, 0), t_piece)

# Add line piece to grid
def update_piece_position(piece):
    previous = []
    for i in range(len(piece.shape)):
        for j in range(len(piece.shape[i])):
            if piece.shape[i][j] == 1:
                grid[piece.y + i][piece.x + j] = 1
                previous.append((piece.y + i, piece.x + j))
    return previous

def remove_previous(previous):
    for i in previous:
        grid[i[0]][i[1]] = 0

previous = update_piece_position(current_piece)
current_piece.move_down()
remove_previous(previous)
previous = update_piece_position(current_piece)
print(grid)

# pygame loop

running = True

var1 = 0

while running:
    previous = update_piece_position(current_piece)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_piece.move_left()
            if event.key == pygame.K_RIGHT:
                current_piece.move_right()
            if event.key == pygame.K_DOWN:
                print(current_piece.y + len(current_piece.shape))
                if current_piece.y + len(current_piece.shape) < 20:
                    current_piece.move_down()
                    var1 = 0
            if event.key == pygame.K_UP:
                current_piece.rotate_clockwise()

    if var1 > 0.2 and current_piece.y + len(current_piece.shape) < 20:
        current_piece.move_down()
        var1 = 0

    remove_previous(previous)
    previous = update_piece_position(current_piece)
    
    window.fill((0, 0, 0))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                pygame.draw.rect(window, (255, 255, 255), (j * 20, i * 20, 20, 20))
            if grid[i][j] == 2:
                pygame.draw.rect(window, (255, 0, 0), (j * 20, i * 20, 20, 20))

    pygame.display.update()
    var1 += 0.01
    clock.tick(60)
