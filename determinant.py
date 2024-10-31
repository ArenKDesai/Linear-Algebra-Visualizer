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
        for i in range(3 * 10 * 2): # six steps
            if i == 0:
                a = A[0,0] * A[1,1]
            if i < 1*step_time: # first step
                first_step = f"{A}  First step: Multiply {A[0,0]} with {A[1,1]} for {a}"
                yield first_step

            if i == 1*step_time:
                b = A[1,0] * A[0,1]
            if i > 1*step_time and i < 2*step_time: # second step
                second_step = f"{A}  Second step: Multiply {A[1,0]} with {A[0,1]} for {b}"
                yield second_step

            if i == 2*step_time:
                det = a - b
            if i > 2*step_time and i < 3*step_time: # third step
                third_step = f"{A}  Third step: Subtract the first by the second: {a} - {b} = {det}"
                yield third_step

def determinant(A):
    if A.shape == (2,2):
        TwoByTwoSolver(A).play()
