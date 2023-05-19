from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == '__main__':
    nums1 = [3, 4, 5, 1, 2]
    nums2 = [4, 5, 6, 7, 0, 1, 2]

    s = Solution()
    print(s.findMin(nums1))
    print(s.findMin(nums2))
