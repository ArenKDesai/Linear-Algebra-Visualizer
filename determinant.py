from .inherit_function import IterableFunction
import numpy as np

class DeterminantSolver(IterableFunction):
    def __init__(self, A, run_viz):
        super().__init__(self.twoDsolver(A), run_viz)

    def get_det(self, A):
        if A.shape == (2,2):
            return self.twoDsolver(A)

    def twoDsolver(self, A):
        a = 0
        b = 0
        det = 0
        for i in range(3):
            if i == 0: # first step
                yield f"{A} det(A) = (Top-Left * Bottom-Right) - (Top-Right * Bottom-Left)", 2
            elif i == 1: # second step
                a = A[0,0] * A[1,1]
                b = A[0,1] * A[1,0]
                yield f"{A} ({A[0,0]} - {A[1,1]}) - ({A[0,1]} - {A[1,0]})", 2
            elif i == 2: # third step
                det = a - b
                yield f"{A} {a} - {b} = {det}", 2

        self.solution = det
        self.mark_complete()

def determinant(A, run_viz):
    solver = DeterminantSolver(A, run_viz)
    if A.shape == (2,2):
        solver.play()
    return solver.solution
