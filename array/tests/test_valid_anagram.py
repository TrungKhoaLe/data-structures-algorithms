from ..algorithms.valid_anagram import Solution
import pytest


@pytest.mark.parametrize("first_string, second_string, expected",
                        [("anagram", "nagaram", True),
                         ("rat", "cat", False)])
def test_valid_anagram(first_string, second_string, expected):
    assert Solution.is_anagram(first_string, second_string) == expected
