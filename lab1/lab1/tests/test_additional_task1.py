from lab1.main.tasks.additional_task1.solution_additional1 import SolutionAdditional1


def test_generate_valid():
    solution = SolutionAdditional1()
    solution.set_input(str(10))
    result = solution.execute()[-1]

    assert result == generate_fib(10)


def generate_fib(n):
    if n <= 1:
        return 1
    else:
        return generate_fib(n - 1) + generate_fib(n - 2)
