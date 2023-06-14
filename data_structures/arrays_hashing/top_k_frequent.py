from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # this hash table maps numbers to frequencies
        count = dict()
        # this list of list is used to group frequencies together
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, count in count.items():
            freq[count].append(num)

        result = []

        # loop backward over the freq list
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
                

if __name__ == '__main__':
    example_1 = [1,1,1,2,2,3]
    k = 2
    s = Solution()
    print(s.topKFrequent(example_1, k))
