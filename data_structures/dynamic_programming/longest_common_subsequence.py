class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # create a 2D "dp" array of size (m+1) x (n+1),
        # where m and n are the lengths of text1 and text2
        # respectively.
        m, n = len(text1), len(text2)
        # the first row and column of "dp" are all zeros which represents
        # the case when one of the strings is empty.
        dp = [[0] * (n+1) for _ in range(m+1)]
        print(dp)
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    print(f"i: {i}, j: {j}")
                    print(f"text1: {text1[i-1]}, text2: {text2[j-1]}")
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]

if __name__ == '__main__':
    text1 = "ABCD"
    text2 = "ACED"
    s = Solution()
    print(s.longestCommonSubsequence(text1, text2))
