from .inherit_function import IterableFunction

class ExampleFunction(IterableFunction):
    def __init__(self, n):
        super().__init__(self.run_ex(n))
        # IterableFunctions must send the abstract method their algorithm call

    def run_ex(self, n):
        # The algorithm call must yield steps as a string
        for i in range(n):
            yield str(n-i)

def example(n: int):
    # Consider this a wrapper for the function, so it can be called as a funciton, not a class
    ExampleFunction(n).play()

if __name__ == '__main__':
    example(100)
