from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n

        for i in range(n):
            # stack[-1] is the top element of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        return result


if __name__ == '__main__':
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    s = Solution()
    print(s.dailyTemperatures(temps))
