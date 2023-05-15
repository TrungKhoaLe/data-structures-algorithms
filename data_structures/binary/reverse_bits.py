class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1) # n & 1 is to get the least significant bit of n
            n >>= 1
        return result


if __name__ == '__main__':
    n = 0b00000010100101000001111010011100
    s = Solution()
    assert s.reverseBits(n) == 0b00111001011110000010100101000000
