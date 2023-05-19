from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # a hashmap
        for i, num in enumerate(nums):
            complement = target - num  # 7, 2, -2, -6
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i  # seen{2: 0, 7: 1, 11: 2, 15: 3}
        return []


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))
