from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        max_product = max_so_far

        for i in range(1, len(nums)):
            num = nums[i]

