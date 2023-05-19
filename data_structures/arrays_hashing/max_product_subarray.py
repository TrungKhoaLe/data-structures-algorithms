from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        max_product = max_so_far

        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            max_so_far = max(num, max_so_far * num)
            min_so_far = min(num, min_so_far * num)
            max_product = max(max_product, max_so_far)

        return max_product


if __name__ == '__main__':
    nums1 = [2, 3, -2, 4]
    nums2 = [-2, 0, -1]
    s = Solution()
    print(s.maxProduct(nums1))
    print(s.maxProduct(nums2))
