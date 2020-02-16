from lab1.main.tasks.task1.solution1 import Solution1
from lab1.main.tasks.task2.solution2 import Solution2
from lab1.main.tasks.task3.solution3 import Solution3
from lab1.main.tasks.task4.solution4 import Solution4

from lab1.main.tasks.additional_task1.solution_additional1 import SolutionAdditional1

INPUT_FILE_ARGUMENT_NAME = 'inputFile'
TASK_ARGUMENT_NAME = 'task'

AVAILABLE_SOLUTIONS = {
    'task1': Solution1,
    'task2': Solution2,
    'task3': Solution3,
    'task4': Solution4,
    'additional1': SolutionAdditional1
}