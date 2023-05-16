from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp represents the minimum number of coins required to
        # make up each amount from 0 to *amount*. Thinking of dp
        # as a cache to store subproblems
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        # dp = [0 , inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
        # i = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
        # coins = [1, 2, 5]
        for i in range(1, amount + 1):
            for coin in coins:
                # if the following condition is valid, we can consider
                # using the current coin to make up the amount i.
                if i - coin >= 0:
                    # update dp[i]
                    # dp[i - coin] represents the number of coins needed to make up the 
                    # the remaining amount after using the current coin, plus one additional
                    # coin for using the current coin itself.
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == '__main__':
    coins = [1, 3, 4, 5]
    amount = 7
    s = Solution()
    assert s.coinChange(coins, amount) == 2
