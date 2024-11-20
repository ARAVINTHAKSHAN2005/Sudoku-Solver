import pygame
import time


### MAIN FILE 

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize the board with some empty and filled values
board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

# Define the window size and cell size
WIDTH, HEIGHT = 540, 540
CELL_SIZE = WIDTH // 9

# Initialize Pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver Visualization")

def is_valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            draw_board(board, current_cell=(row, col))
            pygame.time.delay(10)  # Delay for visualization

            if solve_sudoku(board):
                return True

            board[row][col] = 0
            draw_board(board, backtrack_cell=(row, col))
            pygame.time.delay(10)  # Delay for visualization

    return False

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, column
    return None

def draw_board(board, current_cell=None, backtrack_cell=None):
    WIN.fill(WHITE)

    # Draw grid
    for i in range(10):
        thickness = 1 if i % 3 else 3
        pygame.draw.line(WIN, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)
        pygame.draw.line(WIN, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)

    # Draw numbers and color cells
    font = pygame.font.Font(None, 40)
    for i in range(9):
        for j in range(9):
            number = board[i][j]
            if number != 0:
                color = BLACK  # Default color for pre-filled numbers
                if (i, j) == current_cell:
                    color = YELLOW
                elif (i, j) == backtrack_cell:
                    color = RED
                text = font.render(str(number), True, color)
                WIN.blit(text, (j * CELL_SIZE + 20, i * CELL_SIZE + 10))

    pygame.display.update()

def main():
    # Run the solve algorithm once and visualize it
    solve_sudoku(board)

    # Main loop to keep the window open after solving
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Solved Board !")
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
