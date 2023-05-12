class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
            To solve this problem, we can use bitwise operators. Specifically, we can use
            the bitwise XOR (^) and AND (&) operators to simulate the addition.
            The logic table of XOR:
            A | B | Q 
            0 | 0 | 0 
            0 | 1 | 1
            1 | 0 | 1
            1 | 1 | 0
        """

        while b != 0:
            # e.g. a: 0000 0111, b: 0000 1001
            # carry = a & b = 0000 0001
            # a = a ^ b = 0000 0011
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a


if __name__ == '__main__':
    a = 7
    b = 9
    s = Solution()
    print(s.getSum(a, b))
