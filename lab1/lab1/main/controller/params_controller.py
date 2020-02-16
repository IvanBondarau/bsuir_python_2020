from lab1.main.factory.solution_factory import SolutionFactory
from lab1.main.util.args_parser import ArgsParser


class CommandLineParamsController:

    def __init__(self):
        self.__solution_factory = SolutionFactory()
        self.__argument_parser = ArgsParser()

    def run(self):
        command_line_params = self.__argument_parser.parse()
        solution = self.__solution_factory.create(command_line_params)
        print(solution.execute())