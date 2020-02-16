from lab1.main.tasks.task4.merge_sort import MergeSort
from lab1.main.util.array_parsers import parse_numerical_array

class Solution4:

    def __init__(self):
        self.__merge_sort = None

    def set_input(self, input_str):
        array = parse_numerical_array(input_str)
        self.__merge_sort = MergeSort(array)

    def execute(self):
        return self.__merge_sort.sort()
