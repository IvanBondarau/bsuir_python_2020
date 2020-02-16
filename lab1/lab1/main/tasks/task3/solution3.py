from lab1.main.tasks.task3.quick_sort import QuickSort
from lab1.main.util.array_parsers import parse_numerical_array


class Solution3:

    def __init__(self):
        self.__quick_sort = None

    def set_input(self, input_str):
        array = parse_numerical_array(input_str)
        self.__quick_sort = QuickSort(array)

    def execute(self):
        return self.__quick_sort.sort()
