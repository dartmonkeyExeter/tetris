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
        self.x -= 1
        if self.x < 0:
            self.x = 9
    
    def move_right(self):
        self.x += 1
        if self.x > 9:
            self.x = 0
    def rotate_clockwise(self):
        self.shape = np.rot90(self.shape)
        self.rotation += 1
        if self.rotation == 4:
            self.rotation = 0
    
    def rotate_counter_clockwise(self):
        self.shape = np.rot90(self.shape, 3)
        self.rotation -= 1
        if self.rotation == -1:
            self.rotation = 3

grid = np.zeros((20, 10))

line_piece = [
    [1],
    [1],
    [1],
    [1]
]

t_piece = [
    [0, 1, 0],
    [1, 1, 1]
]

example = tetronimo(5, 0, (255, 0, 0), t_piece)

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

previous = update_piece_position(example)
example.move_down()
example.rotate_counter_clockwise()
remove_previous(previous)
previous = update_piece_position(example)
print(grid)

# pygame loop

running = True

while running:
    previous = update_piece_position(example)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_LEFT:
                    example.move_left()
                if event.key == pygame.K_RIGHT:
                    example.move_right()
                if event.key == pygame.K_DOWN:
                    example.move_down()
                if event.key == pygame.K_UP:
                    example.rotate_clockwise()
                if event.key == pygame.K_SPACE:
                    example.rotate_counter_clockwise()
            except IndexError:
                pass
    remove_previous(previous)
    previous = update_piece_position(example)

    window.fill((0, 0, 0))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                pygame.draw.rect(window, (255, 255, 255), (j * 20, i * 20, 20, 20))

    pygame.display.update()
    print(grid)

    clock.tick(60)
