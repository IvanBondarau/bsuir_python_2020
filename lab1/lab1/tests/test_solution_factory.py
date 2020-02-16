from lab1.main.factory.solution_factory import SolutionFactory
from lab1.main.tasks.task1.solution1 import Solution1
from lab1.main.tasks.task2.solution2 import Solution2
from lab1.main.tasks.task3.solution3 import Solution3
from lab1.main.tasks.task4.solution4 import Solution4
from lab1.main.tasks.additional_task1.solution_additional1 import SolutionAdditional1

factory = SolutionFactory()


def test_task1_valid():
    args = {'task': 'task1', 'inputFile': 'input/text_input.txt'}
    solution = factory.create(args)
    assert type(solution) == Solution1


def test_task2_valid():
    args = {'task': 'task2', 'inputFile': 'input/text_input.txt'}
    solution = factory.create(args)
    assert type(solution) == Solution2


def test_task3_valid():
    args = {'task': 'task3', 'inputFile': 'input/number_array_input.txt'}
    solution = factory.create(args)
    assert type(solution) == Solution3


def test_task4_valid():
    args = {'task': 'task4', 'inputFile': 'input/number_array_input.txt'}
    solution = factory.create(args)
    assert type(solution) == Solution4


def test_task_additional1_valid():
    args = {'task': 'additional1', 'inputFile': 'input/number_input.txt'}
    solution = factory.create(args)
    assert type(solution) == SolutionAdditional1
