from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        To solve this proble, we use a dynamic programming approach.

        1. Create an array *ans* with a length of *n + 1* and initialize
        it with all zeros,

        2. iterate from 1 to *n* (inclusive):
            - set *ans[i]* equal to *ans[i >> 1]* plus the LSB of *i*
            which can be obtained using *i & 1*.

        3. return the resulting *ans* array.
        """
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # e.g. n = 7
            # i = 1, ans[1] = ans[0] + (0001 & 0001) = 1
            # i = 2, ans[2] = ans[1] + (0010 & 0001) = 1
            # i = 3, ans[3] = ans[1] + (0011 & 0001) = 2
            # i = 4, ans[4] = ans[2] + (0100 & 0001) = 1
            # i = 5, ans[5] = ans[2] + (0101 & 0001) = 2
            # i = 6, ans[6] = ans[3] + (0110 & 0001) = 2
            # i = 7, ans[7] = ans[3] + (0111 & 0001) = 3
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


if __name__ == "__main__":
    n = 5
    s = Solution()
    print(s.countBits(n))
