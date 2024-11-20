# #Imports
# from pprint import pprint 

# def empty_slot(puzzle):
#     # finds the next row, col on the puzzle that's nnot filled yet --> represented with -1
#     # return row, col tuple (or (None, None) if there is none)

#     # keep in mind that  0-8 for our indices 
#     for r in range(9):
#         for c in range(9):
#             if puzzle[r][c] == -1: # range(9) is 0,1,2, ... 8
#                 return r, c 
    
#     return None, None # if no empty spaces are available

# def is_valid(puzzle, guess, row, col):
#     # figures out whether the guess at the row/col of the puzzle is a valid guess 
#     # returns True if value is valid, False otherwise 
#     # for a guess to be valid, then we need to follow the sudoku rules
#     # that number must not be repeated in the row, column, or 3x3 square that it appears in
    
#     # Start with row 
#     row_vals = puzzle[row]
#     if guess in row_vals:
#         return False 

#     # The Columns 
#     col_vals = []
#     for i in range(9):
#         col_vals.append(puzzle[i][col])
#         #col_vals = [puzzle[i][col] for i in range(9)]
#     if guess in col_vals:
#         return False

#     # the sqaure
#     row_start = (row // 3) * 3
#     col_start = (col // 3) * 3 

#     for r in range(row_start, row_start+3):
#         for c in range(col_start, col_start +3):
#             if puzzle[r][c] == guess:
#                 return False

#     #if we gethere, the tests are passed
#     return True

# def solve_sudoku(puzzle):
#     # solve sudoku using backtracking 
#     # our puzzle is a list of lists, where eaxh inner list is a row in our sudoku puzzle
#     # return whether a slution exists
#     # muates puzzle to be teh solution (if solution exists)

#     # step 1:choose somewhere on the puzzle to make a guess
#     row, col = empty_slot(puzzle)

#     # step 1.1: if there's nowhere left, then we're done because we omly allowed valid inputs
#     if row == None and col == None :
#         return True 

#     # step 2: if there is a place to put a number, then make a guess between 1 and 9 
#     for guess in range(1,10):
#         #step 3: check if this is valid guess 
#         if is_valid(puzzle, guess, row, col):
#             # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
#             puzzle[row][col] = guess
#             # then call the solve function
#             if solve_sudoku(puzzle):
#                 return True 
#         # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
#         puzzle[row][col] = -1 #reset the game
#     return False

#     #step 6: if none of the numbers that we try work, the puzzle is unsolvable 

# if __name__ == '__main__':

#     example_board = [
#         [-1, -1, -1,   -1, -1, 5,   7, -1, -1],
#         [7, -1, -1,   -1, 9, -1,   -1, -1, -1],
#         [-1, -1, -1,   -1, 6, -1,   -1, -1, -1],

#         [-1, -1, 2,   -1, -1, -1,   -1, 3, -1],
#         [3, -1, 4,   -1, -1, 7,   5, 9, -1],
#         [8, -1, 6,   -1, 5, -1,   2, -1, -1],

#         [-1, -1, -1,   4, -1, -1,   -1, 6, -1],
#         [6, -1, 8,   -1, -1, -1,   3, -1, -1],
#         [-1, -1, 3,   -1, 2, -1,   9, 7, -1]
#     ]

#     print(solve_sudoku(example_board))
#     pprint(example_board)

