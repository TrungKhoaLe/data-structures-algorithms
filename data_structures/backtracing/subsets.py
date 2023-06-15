from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.subset = []
        self._backtrack(0, nums, self.subset, self.result)
        return self.result
    
    def _backtrack(self, index_position: int, nums: List[int], subset: List[int], result: List[int]):
        if index_position >= len(nums):
            result.append(subset.copy())
            return
        # At every element, we have two options, adding that element to the subset or ignore it
        # the following LOCs is for the adding path
        subset.append(nums[index_position])
        self._backtrack(index_position + 1, nums, subset, result)
        # the following LOCs is for the ignoring path
        subset.pop()
        self._backtrack(index_position + 1, nums, subset, result)


if __name__ == '__main__':
    example_1 = [1, 2, 3]
    s = Solution()
    print(s.subsets(example_1))
