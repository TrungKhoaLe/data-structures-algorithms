from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self._backtrack(0, candidates, [], 0, target)
        return self.result

    def _backtrack(self, index_position: int, candidates: List[int], subset: List[int], total: int, target: int):
       if total == target:
            self.result.append(subset.copy())
            return
        if index_position >= len(candidates) or total > target:
            return
        # go to the left of the decision tree
        subset.append(candidates[index_position])
        self._backtrack(index_position, candidates, subset, total + candidates[index_position], target)
        # go to the right of the decision tree
        subset.pop()
        self._backtrack(index_position + 1, candidates, subset, total, target)


if __name__ == '__main__':
    example_1 = [2, 3, 6, 7]
    target = 7
    s = Solution()
    print(s.combinationSum(example_1, target))
