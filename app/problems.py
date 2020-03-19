from random import randint

class Problems:

    def __init__(self):
        self._problems = [
            [
                [7, 8, 0, 4, 0, 0, 1, 2, 0],
                [6, 0, 0, 0, 7, 5, 0, 0, 9],
                [0, 0, 0, 6, 0, 1, 0, 7, 8],
                [0, 0, 7, 0, 4, 0, 2, 6, 0],
                [0, 0, 1, 0, 5, 0, 9, 3, 0],
                [9, 0, 4, 0, 6, 0, 0, 0, 5],
                [0, 7, 0, 3, 0, 0, 0, 1, 2],
                [1, 2, 0, 0, 0, 7, 4, 0, 0],
                [0, 4, 9, 2, 0, 6, 0, 0, 7]
            ],
            [
                [0, 2, 0, 5, 0, 3, 0, 0, 1],
                [0, 5, 0, 0, 0, 0, 3, 4, 9],
                [0, 7, 0, 1, 9, 0, 0, 5, 6],
                [0, 0, 0, 0, 0, 0, 7, 0, 0],
                [7, 3, 0, 2, 0, 0, 5, 0, 8],
                [0, 0, 5, 0, 7, 4, 1, 3, 0],
                [0, 0, 8, 3, 0, 9, 0, 0, 0],
                [3, 0, 2, 0, 0, 6, 9, 0, 0],
                [1, 9, 7, 0, 5, 2, 6, 0, 3],
            ],
            [
                [9, 0, 1, 5, 6, 8, 0, 0, 0],
                [0, 0, 8, 3, 0, 2, 9, 0, 5],
                [2, 0, 5, 1, 0, 0, 0, 0, 3],
                [4, 0, 0, 0, 0, 5, 1, 0, 2],
                [0, 0, 0, 7, 3, 4, 0, 0, 0],
                [5, 8, 0, 0, 0, 0, 7, 6, 0],
                [0, 0, 0, 4, 0, 3, 2, 5, 0],
                [7, 0, 2, 0, 5, 1, 3, 4, 9],
                [0, 0, 0, 9, 2, 0, 0, 0, 0],
            ],
        ]

    def random_problem(self):
        n = randint(0, len(self._problems) - 1)
        return self._problems[n]