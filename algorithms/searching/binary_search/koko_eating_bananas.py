from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = float("inf")

        while l <= r:
            m = (l + r) // 2
            # check whether Koko has finished eating all bananas with this eating speed
            h_prime = sum([ceil(pile/m) for pile in piles])
            if h_prime <= h:
                k = min(m, k)
                r = m - 1
            else:
                l = m + 1

        return k


if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    h = 8
    s = Solution()
    print(s.minEatingSpeed(piles, h))
