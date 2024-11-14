# Sudoku-Solver
Python Program that, solves any solvable Sudoku Puzzle using a backtracking algorithm.

### This Sudoku Solver uses a Backtracking Algorithm.  
A backtracking algorithm is a problem-solving algorithm that uses a brute force approach for finding the desired output.  
The Brute force approach tries out all the possible solutions and chooses the desired/best solutions.

* The Sudoku Board is represented in a Nested List where '-1' stands for the unfilled/empty spaces on the board
* It starts off my entering the first number that suits a particular space on the board according to the classic Sudoku rules 
* It keeps on enetring suiting numbers until at one point either the puzzle is solved or no number can satisfy the condition 
* Then it changes numbers as it backtracks until the whole board is completed, this can happen multiple times 
* After all tries if none of the number works teh puzzle is unsolvable. 

![image](https://github.com/user-attachments/assets/3c94647e-d3ea-4136-b40d-f41f6e314671)
