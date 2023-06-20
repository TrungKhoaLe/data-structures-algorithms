class Solution:
    def ispalinDrome(self, s: str) -> bool:

        s = "".join([c for c in s if c.isalnum()]).lower()
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    test_string = "A man, a plan, a canal: Panama"
    s = Solution()
    print(s.ispalinDrome(test_string))
