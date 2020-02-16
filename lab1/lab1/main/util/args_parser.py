import argparse

from lab1.main.application_constants import INPUT_FILE_ARGUMENT_NAME, TASK_ARGUMENT_NAME, AVAILABLE_SOLUTIONS


class ArgsParser:
    def __init__(self):
        self.__parser = argparse.ArgumentParser()
        self.__parser.add_argument('task', type=str, choices=list(AVAILABLE_SOLUTIONS.keys()))
        self.__parser.add_argument('input', type=str)

    def parse(self):
        args = self.__parser.parse_args()

        return {INPUT_FILE_ARGUMENT_NAME: args.input, TASK_ARGUMENT_NAME: args.task}


