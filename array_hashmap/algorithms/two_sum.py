from typing import List


class Solution:
    @classmethod
    def two_sum(cls, nums: List[int],
                target: int) -> List[int]:
        # this is used to map numbers to indices
        tracking_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in tracking_map:
                return [tracking_map[diff], i]
            tracking_map[n] = i
