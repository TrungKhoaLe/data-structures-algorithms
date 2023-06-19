from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # Another way we could do is to use this formula: l + ((r - l) // 2)
            # to prevent overflow if l and r are too big
            m = (l + r) // 2 

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1


if __name__ == '__main__':
    ex_nums = [-1, 0, 3, 5, 9, 12]
    ex_target = 9
    s = Solution()
    print(s.search(ex_nums, ex_target))
