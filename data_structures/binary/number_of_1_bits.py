class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += n & 1 # e.g. 0000 0001 & 0000 0111 -> 0000 0001 (1)
            n >>= 1
        return count


if __name__ == '__main__':
    n = 7
    s = Solution()
    print(s.hammingWeight(n))
