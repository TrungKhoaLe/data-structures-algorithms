from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        cur_min = float("inf")

        while l < r:
            mid = (l + r) // 2

            cur_min = min(cur_min, nums[mid])

            # min is in the right side
            if nums[mid] > nums[r]:
                l = mid + 1

            else:
                r = mid - 1

        return min(cur_min, nums[l])

if __name__ == '__main__':
    nums = [6, 7, 0, 1, 2, 3, 4, 5, 6]
    s = Solution()
    print(s.findMin(nums))
