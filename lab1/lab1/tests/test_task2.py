import pytest

from lab1.main.tasks.task2.solution2 import Solution2


def test_simple_text_valid():
    solution2 = Solution2()
    solution2.set_input('a a b b b b b c c c d d d d d d')
    result = solution2.execute()
    answer = 'd b c a'
    assert answer == result


def test_empty_text_valid():
    solution2 = Solution2()
    solution2.set_input('')
    result = solution2.execute()
    answer = ''
    assert answer == result


def test_empty_text_value_error():
    with pytest.raises(ValueError) as error:
        solution2 = Solution2()
        result = solution2.execute()
