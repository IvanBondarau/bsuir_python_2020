import pytest

from lab1.main.tasks.task1.solution1 import Solution1


def test_text_valid():
    solution = Solution1()
    solution.set_input('B Foo Bar Foo B Foo B B')
    result = solution.execute()
    answer = {'B': 4, 'Foo': 3, 'Bar': 1}
    assert answer == result


def test_empty_input_valid():
    solution = Solution1()
    solution.set_input('')
    result = solution.execute()
    assert len(result) == 0


def test_empty_text_value_error():
    with pytest.raises(ValueError) as error:
        solution = Solution1()
        result = solution.execute()
