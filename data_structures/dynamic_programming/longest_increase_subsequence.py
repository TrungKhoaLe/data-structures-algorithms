from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
 
if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    s = Solution()
    print(s.lengthOfLIS(nums))
