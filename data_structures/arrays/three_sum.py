from typing import List


class Solution:
    """ To solve this problem, we can use the two pointer appoach
        along with sorting the array.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        # iterate over the sorted array "nums" up to the second-to-last element
        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # skip the current iteration to avoid duplicate triplets
                continue
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # skip duplicate triplets
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # change left and right at the same time as if right didn't change, we could
                    # receive a sum that is greater than zero due to the sorted array.
                    left += 1
                    right -= 1
                elif curr_sum < 0:
                    # increment the 'left' pointer to consider a larger element
                    left += 1
                else:
                    # decrement the 'right' pointer to consider a smaller element
                    right -= 1
        return result

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    nums1 = [0, 1, 1]
    nums2 = [-2, 0, 3, -1, 4, 0, 3, 4, 1, 1, 1, -3, -5, 4, 0]
    s = Solution()
    print(s.threeSum(nums))
    print(s.threeSum(nums1))
    print(s.threeSum(nums2))
