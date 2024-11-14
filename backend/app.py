from flask import Flask, jsonify, render_template, request
from pprint import pprint

app = Flask(__name__)

def empty_slot(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    # Check row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Check column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Check 3x3 square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    row, col = empty_slot(puzzle)
    if row is None and col is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
            puzzle[row][col] = -1

    return False

@app.route('/solve', methods=['POST'])
def solve_puzzle():
    puzzle = request.get_json()
    # Convert the flat list into a 2D list
    solved_puzzle = [puzzle[i:i+9] for i in range(0, len(puzzle), 9)]
    if solve_sudoku(solved_puzzle):
        return jsonify(solved_puzzle)
    else:
        return jsonify({'error': 'Puzzle is unsolvable'}), 400

@app.route('/')
def index():
    example_board = [
        [-1, -1, -1,   -1, -1, 5,   7, -1, -1],
        [7, -1, -1,   -1, 9, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, 6, -1,   -1, -1, -1],

        [-1, -1, 2,   -1, -1, -1,   -1, 3, -1],
        [3, -1, 4,   -1, -1, 7,   5, 9, -1],
        [8, -1, 6,   -1, 5, -1,   2, -1, -1],

        [-1, -1, -1,   4, -1, -1,   -1, 6, -1],
        [6, -1, 8,   -1, -1, -1,   3, -1, -1],
        [-1, -1, 3,   -1, 2, -1,   9, 7, -1]
    ]
    return render_template('index.html', example_board=example_board)

if __name__ == '__main__':
    app.run(debug=True)