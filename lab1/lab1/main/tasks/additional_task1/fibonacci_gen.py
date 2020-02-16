class FibonacciGenerator:

    def __init__(self):
        self.__previous_fib = 0
        self.__current_fib = 1

    def generate(self):
        next_fib = self.__current_fib + self.__previous_fib
        self.__previous_fib = self.__current_fib
        self.__current_fib = next_fib
        return self.__current_fib
