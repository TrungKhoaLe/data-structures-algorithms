from typing import List


class Solution:
    """
    This solution uses Kadane's algorithm. The algorithm looks for all
    positive contiguous segments of the array and keeps track of the
    maximum sum contiguous subarray among all positive segments.
    """
    def maxSubarray(self, nums: List[int]) -> int:
        # this variable is used to store the max sum of the 
        # contiguous subarray found so far
        max_so_far = float('-inf')
        # this variable is used to store the max sun of the
        # contiguous subarray ending at the current index
        max_ending_here = 0
        
        for num in nums:
            print(f"num: {num}\n")
            max_ending_here += num
            max_so_far = max(max_so_far, max_ending_here)
            print(f"max: {max_so_far}")
            max_ending_here = max(0, max_ending_here)
        
        return max_so_far


if __name__ == '__main__':
    s = Solution()
    # max_ending_here = [-2, 1, -2, 4, 3, 5, 6, 1, 5] 
    # max_so_far = [-2, 1, 1, 4, 4, 5, 6, 6, 6]
    # max_ending_here = [0, 1, 0, 4, 3, 5, 6, 1, 5]
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubarray(nums))
