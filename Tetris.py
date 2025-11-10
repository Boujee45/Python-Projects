import pygame
import random

pygame.init()
screen = pygame.display.set_mode((300,600))

pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
grid = [[0 for _ in range(10)] for _ in range(20)]

shapes = [[[1,1,1,1]],  #I
          [[1,1],[1,1]], #O
          [[1,1,1],[0,1,0]], #T
         [[1,1,1],[1,0,0]], #J
          [[1,1,1],[0,0,1]], #L
          [[1,1,0],[0,1,1]], #Z
          [[0,1,1],[1,1,0]]] #S

colors = [(255,0,0),
          (0,255,0),
          (0,0,255),
          (255,255,0),
          (255,0,255),
          (0,255,255),
          (255,165,0)
          ]
current_shape = random.choice(shapes)
current_color = random.choice(colors)
shape_x, shape_y = 3, 0
score = 0
font = pygame.font.Font(None, 36)

def can_move(shape, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell and (x+j < 0 or x+j >= 10 or y+i >= 20 or (y+i >= 0 and grid[y+i][x+j])):
                return False
    return True

def place_shape():
    global current_shape, current_color
    global shape_x, shape_y, score
    for i, row in enumerate(current_shape):
        for j, cell in enumerate(row):
            if cell:
                grid[shape_y+i][shape_x+j] = current_color
    for i in range(19, -1, -1):
        if all(grid[i]):
            del grid[i]
            grid.insert(0, [0 for _ in range(10)])
            score += 100
    current_shape = random.choice(shapes)
    current_color = random.choice(colors)
    shape_x, shape_y = 3, 0

running = True
fall_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and can_move(current_shape, shape_x-1, shape_y):
                shape_x -= 1
            elif event.key == pygame.K_RIGHT and can_move(current_shape, shape_x+1, shape_y):
                shape_x += 1
            elif event.key == pygame.K_DOWN and can_move(current_shape, shape_x, shape_y+1):
                shape_y += 1

    fall_time += clock.get_time()
    if fall_time >= 500:
        if can_move(current_shape, shape_x, shape_y+1):
            shape_y += 1
        else:
            place_shape()
        fall_time = 0

    screen.fill((0,0,0))
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen,cell,(j*30, i*30, 30, 30))

    for i, row in enumerate(current_shape):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, current_color,
            ((shape_x+j)*30, (shape_y+i)*30, 30, 30))

    score_text = font.render(f"Score: {score}",
                            True, (255, 255, 255))
    screen.blit(score_text, (10,10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

#Tetris 2
'''import pygame, random

# Initialize Pygame
pygame.init()

# Grid dimensions
COLS, ROWS = 10, 20
CELL_SIZE = 30
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Colors
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0)     # Z
]

# Shapes (Tetrominoes)
SHAPES = [
    [[1, 1, 1, 1]],                # I
    [[1, 0, 0], [1, 1, 1]],        # J
    [[0, 0, 1], [1, 1, 1]],        # L
    [[1, 1], [1, 1]],              # O
    [[0, 1, 1], [1, 1, 0]],        # S
    [[0, 1, 0], [1, 1, 1]],        # T
    [[1, 1, 0], [0, 1, 1]]         # Z
]

# Create empty grid
def create_grid():
    return [[BLACK for _ in range(COLS)] for _ in range(ROWS)]

# Draw grid & blocks
def draw_grid(grid):
    for y in range(ROWS):
        for x in range(COLS):
            pygame.draw.rect(screen, grid[y][x], (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)
            pygame.draw.rect(screen, GRAY, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Piece class
class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS)

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]  # Rotate 90°

# Check valid position
def valid_position(piece, grid, offset=(0,0)):
    off_x, off_y = offset
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = piece.x + x + off_x
                new_y = piece.y + y + off_y
                if new_x < 0 or new_x >= COLS or new_y >= ROWS:
                    return False
                if new_y >= 0 and grid[new_y][new_x] != BLACK:
                    return False
    return True

# Lock piece into grid
def lock_piece(piece, grid):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                grid[piece.y + y][piece.x + x] = piece.color

# Clear full rows
def clear_rows(grid):
    cleared = 0
    for y in range(ROWS):
        if BLACK not in grid[y]:
            del grid[y]
            grid.insert(0, [BLACK for _ in range(COLS)])
            cleared += 1
    return cleared

# Game loop
grid = create_grid()
current_piece = Piece(COLS//2 - 2, 0, random.choice(SHAPES))
clock = pygame.time.Clock()
fall_time = 0
fall_speed = 500  # milliseconds
running = True

while running:
    screen.fill(BLACK)
    draw_grid(grid)

    # Draw current piece
    for y, row in enumerate(current_piece.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, current_piece.color, ((current_piece.x+x)*CELL_SIZE, (current_piece.y+y)*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

    # Timer for falling
    fall_time += clock.get_rawtime()
    clock.tick()
    if fall_time > fall_speed:
        fall_time = 0
        if valid_position(current_piece, grid, (0,1)):
            current_piece.y += 1
        else:
            lock_piece(current_piece, grid)
            clear_rows(grid)
            current_piece = Piece(COLS//2 - 2, 0, random.choice(SHAPES))
            if not valid_position(current_piece, grid):
                running = False  # Game over

    # Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and valid_position(current_piece, grid, (-1,0)):
                current_piece.x -= 1
            if event.key == pygame.K_RIGHT and valid_position(current_piece, grid, (1,0)):
                current_piece.x += 1
            if event.key == pygame.K_DOWN and valid_position(current_piece, grid, (0,1)):
                current_piece.y += 1
            if event.key == pygame.K_UP:
                current_piece.rotate()
                if not valid_position(current_piece, grid):
                    current_piece.rotate()
                    current_piece.rotate()
                    current_piece.rotate()

pygame.quit()
'''