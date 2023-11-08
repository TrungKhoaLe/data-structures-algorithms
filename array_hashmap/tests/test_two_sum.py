from ..algorithms.two_sum import Solution
import pytest


@pytest.mark.parametrize("input, target, expected",
                         [([2, 7, 11, 15], 9, [0, 1]),
                          ([3, 2, 4], 6, [1, 2]),
                          ([3, 3], 6, [0, 1])])
def test_two_sum(input, target, expected):
    assert Solution.two_sum(input, target) == expected
