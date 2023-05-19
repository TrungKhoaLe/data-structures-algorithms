from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """ To solve this problem, we can use the two pointer approach. We start with two pointers,
            one the beginning of the array and one at the end. We calculate the area between two lines
            and move the pointer that corresponds to the shorted line towards the center. This way, we
            are trying to maximize the area by adjusting the width of the container and keeping the height
            as large as possible.
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    print(s.maxArea(height))
