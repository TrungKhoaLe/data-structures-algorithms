from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n  # create an array of length n
        right_products = [1] * n  # create an  array of length n
        output = [1] * n  # create an array of length n
        
        # calculate the products of all elements to the left of the current element
        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i-1]

        # calculate the products of all elements to the right of the current element
        for i in range(n-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]

        # calculate the product of left_products and right_products
        for i in range(n):
            output[i] = left_products[i] * right_products[i]
        return output


if __name__ == '__main__':
    input_vals = [1, 2, 3, 4]
    s = Solution()
    print(s.productExceptSelf(input_vals))
