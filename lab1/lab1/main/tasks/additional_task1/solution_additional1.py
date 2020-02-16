from lab1.main.tasks.additional_task1.fibonacci_gen import FibonacciGenerator


class SolutionAdditional1:

    def __init__(self):
        self.__num_of_generated = None

    def set_input(self, input_str):
        self.__num_of_generated = int(input_str)

    def execute(self):
        fib_generator = FibonacciGenerator()

        generated = []
        for _ in range(self.__num_of_generated):
            generated.append(fib_generator.generate())

        return generated


