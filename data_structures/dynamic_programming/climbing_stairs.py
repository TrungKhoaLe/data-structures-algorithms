class Solution:
    def climbStairs(self, n: int) -> int:
        """
        To solve this problem, we can use the dynamic programming approach.

        1. Base cases:
            - dp[1] = 1: There is only one way to reach step 1, taking 1 step,
            - dp[2] = 2: Two ways to reach step 2, taking 1 step twice or take 2 steps at once.
        2. For step 3:
            - We have two options: take 1 step from step 2 or take 2 steps from step 1,
            - so, dp[3] = d[2] + dp[1] = 2 + 1 = 3
        3. For step 4:
            - We can either take 1 step from step 3 or take 2 steps from step 2,
            - so, dp[4] = dp[3] + dp[2] = 3 + 2 = 5
        4. For further steps:
            - Same explanation, the generalized formula is dp[i] = dp[i-1] + dp[i-2]
        """
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1   # there is only one way to climb the first step
        dp[2] = 2   # there are two ways to climb the second step.
                    # For example, 1 step + 1 step or 2 steps
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i -2]
        return dp[n]

if __name__=='__main__':
    n = 4
    s = Solution()
    print(s.climbStairs(n))
