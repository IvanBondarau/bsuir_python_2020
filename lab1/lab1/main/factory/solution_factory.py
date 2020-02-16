from lab1.main.application_constants import TASK_ARGUMENT_NAME, INPUT_FILE_ARGUMENT_NAME, AVAILABLE_SOLUTIONS
from lab1.main.util.files import read_input_from_file


class SolutionFactory:

    def create(self, args):

        input_file_name = args[INPUT_FILE_ARGUMENT_NAME]
        file_input = read_input_from_file(input_file_name)

        task_name = args[TASK_ARGUMENT_NAME]
        solution = AVAILABLE_SOLUTIONS[task_name]()
        solution.set_input(file_input)

        return solution






