from is_duplicated import Solution
import pytest


@pytest.mark.parametrize("input_array, expected", [([1, 2, 3, 1], True),
                                                   ([1, 2, 3, 4], False),
                                                   ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)])
def test_is_duplicated(input_array, expected):
    assert Solution.contains_duplicates(input_array) == expected
