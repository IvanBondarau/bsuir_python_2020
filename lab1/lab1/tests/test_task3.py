from lab1.main.tasks.task3.solution3 import Solution3


def test_sort_valid():
    str_input = '4 7 6.6 4 9 11.7 120 33'
    solution = Solution3()
    solution.set_input(str_input)
    result = solution.execute()
    answer = sorted(list(map(float, str_input.split())))
    assert answer == result


def test_sort_one_element_valid():
    str_input = '30'
    solution = Solution3()
    solution.set_input(str_input)
    result = solution.execute()
    answer = sorted(list(map(float, str_input.split())))
    assert answer == result


def test_sort_empty_array_valid():
    str_input = ''
    solution = Solution3()
    solution.set_input(str_input)
    result = solution.execute()
    answer = sorted(list(map(float, str_input.split())))
    assert answer == result
