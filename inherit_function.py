from abc import ABC, abstractmethod
import time
import os

LINE_CLEAR = '\x1b[2K' # Enables clearing stdout

class IterableFunction(ABC):
    """
    The generic function that other linear algebra functions will inherit. 
    """
    def __init__(self, algorithm):
        self.complete = False
        self.algorithm = algorithm
        self.solution = None

    def mark_complete(self):
        self.complete = True

    def play(self):
        """
        Displays the visualization of the algorithm or function. 
        NOTE: algorithms must yield their steps as a string. 
        """
        while not self.complete:
            try:
                step, length = next(self.algorithm)
                print(step)
                time.sleep(length)

            except StopIteration:
                self.mark_complete()
