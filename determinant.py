from .inherit_function import IterableFunction
import numpy as np

class TwoByTwoSolver(IterableFunction):
    # TODO: update this to accomodate for lists
    def __init__(self, A):
        super().__init__(self.run_solver(A))

    def run_solver(self, A):
        step_time = 10*2 # each yield is 0.1 seconds, so each step will be 0.1*10*2 for 2 seconds
        a = 0
        b = 0
        det = 0
        length = 2 # two seconds per step
        for i in range(3):
            if i == 0: # first step
                yield f"{A} det(A) = (Top-Left * Bottom-Right) - (Top-Right * Bottom-Left)", 2
            elif i == 1:
                a = A[0,0] * A[1,1]
                b = A[0,1] * A[1,0]
                yield f"{A} ({A[0,0]} - {A[1,1]}) - ({A[0,1]} - {A[1,0]})", 2
            elif i == 2:
                det = a - b
                yield f"{A} {a} - {b} = {det}", 2

        self.solution = det

def determinant(A):
    solver = TwoByTwoSolver(A)
    if A.shape == (2,2):
        solver.play()
    return solver.solution
