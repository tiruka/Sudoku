# Sudoku Algorithm

Algorithms and visualizations of Sudoku

## What is Sudoku

Sudoku (数独, sūdoku, digit-single) is a logic-based, combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution. ([Wikipedia](https://en.wikipedia.org/wiki/Sudoku))
As algorithm, it can be sovled by DFS(Depth First Search) with Backtraking. I guess it is smillar to 8 Queens Problem in the aspect of the timing and method of usign backtraking.

## Set up

Please Git-clone this repository and hit the below commands at first to set up necessary libraries. If your pc is Mac and its os is newer than Mojave, you should use `requirements_for_over_mojava.txt` instead.

```:sh
pip install -r requirements.txt
```

There you go, you can play the Sudoku Game with the commands runngin Pygame.

```:sh
python gui_game.py
```

## How to Play

Click a box and hit a number on your keybaord and press the ENTER key. If it fails, you will get a failure mark (like X in red). If it is correct, the number is put on.
Is it to difficult to sovle? Don't worry! You can get a answer by pressing SPACE! You can see the dfs and backtraking algorithms is going to sovle it with tiral and erros.
