from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        This solution utilizes the binary search algorithm to find the target
        element in the rotated sorted array.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # The rotation did happen.
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1 # target is situated in the first half of the array
                else:
                    left = mid + 1
            # The rotation did not happen.
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    s = Solution()
    print(s.search(nums, target))
