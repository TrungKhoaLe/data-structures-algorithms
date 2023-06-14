from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if not strs:
            return [[""]]

        result = {}

        for word in strs:

            # sorted function will create a list of sorted
            # characters of a word. We need to join the 
            # characters again to form a sorted word
            sorted_word = "".join(sorted(word))

            if sorted_word in result:
                result[sorted_word].append(word)
            else:
                result[sorted_word] = [word]

        return list(result.values())

if __name__ == '__main__':
    example_1 = ["eat","tea","tan","ate","nat","bat"]
    s = Solution()
    print(s.groupAnagrams(example_1))

