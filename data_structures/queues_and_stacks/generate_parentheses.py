from typing import List


class Solution:
    def generateParentheses(self, n: int) -> List[str]:
        result = []
        stack = []
        self.backtrack(result, stack, n, n)
        return result

    def backtrack(self, result, stack, left, right):
        # left is the number of remaining open parentheses.
        # right is the number of remaining closed parentheses.
        # NOTE: Only add open parenthesis if left <= n
        # NOTE: Only add closing parenthesis if right <= left
        print("++++++++++++++++++++")
        print(f"Left: {left}")
        print(f"Right: {right}")
        print(f"Stack: {stack}")
        print("++++++++++++++++++++\n")
        if left == 0 and right == 0:
            result.append("".join(stack))
            return
        
        if left > 0:
            stack.append("(")
            self.backtrack(result, stack, left - 1, right)
            stack.pop()

        if right > left:
            stack.append(")")
            self.backtrack(result, stack, left, right - 1)
            stack.pop()


if __name__ == "__main__":
    n = 3
    s = Solution()
    print(s.generateParentheses(n))
