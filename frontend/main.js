const sudokuBoard = document.getElementById('sudoku-board');
const solveButton = document.getElementById('solve-button');

// Initialize the Sudoku board
const initBoard = (puzzle) => {
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      const cell = document.createElement('div');
      cell.classList.add('sudoku-cell', 'border', 'border-gray-400', 'text-center', 'text-2xl', 'font-bold');
      cell.dataset.row = i;
      cell.dataset.col = j;
      cell.textContent = puzzle[i][j] === -1 ? '-' : puzzle[i][j].toString();
      sudokuBoard.appendChild(cell);
    }
  }
};

// Handle user input on the Sudoku board
sudokuBoard.addEventListener('click', (event) => {
  if (event.target.classList.contains('sudoku-cell')) {
    const row = parseInt(event.target.dataset.row);
    const col = parseInt(event.target.dataset.col);
    // Add logic to handle user input and update the board
  }
});

// Solve the Sudoku puzzle
solveButton.addEventListener('click', async () => {
  const cells = sudokuBoard.querySelectorAll('.sudoku-cell');
  const puzzle = [];
  cells.forEach((cell) => {
    const value = cell.textContent === '-' ? -1 : parseInt(cell.textContent);
    puzzle.push(value);
  });

  try {
    const response = await fetch('/solve', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(puzzle),
    });

    if (response.ok) {
      const solvedPuzzle = await response.json();
      updateBoard(solvedPuzzle);
    } else {
      const error = await response.json();
      console.error(error.error);
    }
  } catch (error) {
    console.error('Error solving Sudoku:', error);
  }
});

const updateBoard = (puzzle) => {
  const cells = sudokuBoard.querySelectorAll('.sudoku-cell');
  cells.forEach((cell, index) => {
    cell.textContent = puzzle[index] === -1 ? '-' : puzzle[index].toString();
  });
};

// Initialize the board with the example puzzle
initBoard({{ example_board|tojson }});