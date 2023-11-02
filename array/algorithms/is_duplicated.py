from typing import List


class Solution:
    @classmethod
    def contains_duplicates(cls, nums: List[int]):
        met = set()
        for item in nums:
            if item in met:
                return True
            met.add(item)
        return False
