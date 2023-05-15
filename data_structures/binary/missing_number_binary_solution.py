from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        To solve this problem, we can do the XOR of n (missing) with each index and value
        """
        missing = len(nums)

        for i, num in enumerate(nums):
            # e.g. nums = [3, 0, 1], range = [0, 3]
            # missing = 3, i = 0, num = 3, missing = missing ^ i ^ num = 0011 ^ 0000 ^ 0011 = 0011 ^ 0011 = 0
            # missing = 0, i = 1, num = 0, missing = missing ^ i ^ num = 0000 ^ 0001 ^ 0000 = 0001 ^ 0000 = 1
            # missing = 1, i = 2, num = 1, missing = missing ^ i ^ num = 0001 ^ 0010 ^ 0001 = 0011 ^ 0001 = 2
            missing ^= i ^ num

        return missing


if __name__ == '__main__':
    nums = [3, 0, 1]
    s = Solution()
    print(s.missingNumber(nums))
