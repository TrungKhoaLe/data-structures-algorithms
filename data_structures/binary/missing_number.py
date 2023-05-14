from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        To solve this problem, we can calculate the expected sum of the
        range [0, n] using the formula *(n x (n + 1)) // 2*. Then, we
        calculate the actual sum of the elements in *nums* array using
        *sum()* function. The missing number is simply the difference
        between the expected sum and the actual sum.

        The solution has a time complexity of O(n) since it iterates over
        *nums* array once to calculate the sum. It uses O(1) extra space
        since it only uses a constant amount of space to store variables
        *n*, *expected_sum*, and *actual_sum*.
        """
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)

        missing_num = expected_sum - actual_sum

        return missing_num


if __name__ == '__main__':
    nums = [3, 0, 1]
    s = Solution()
    print(s.missingNumber(nums))
        
