from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True

            seen.add(num)
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1, 1, 2, 3, 4]))
    print(s.containsDuplicate([1, 2, 3]))
