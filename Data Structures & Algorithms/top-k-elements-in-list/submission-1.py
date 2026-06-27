import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        max_freq = max(freq.values())

        temp = [[] for _ in range(max_freq + 1)]

        for num, count in freq.items():
            temp[count].append(num)
        result = []
        for i in range(max_freq, 0, -1):
            for num in temp[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result



        