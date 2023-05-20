from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in nums:
            # check if the current number is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # update the longest streak
                longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    s = Solution()
    print(s.longestConsecutive(nums))
