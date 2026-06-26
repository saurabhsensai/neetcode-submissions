import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num)) 

            if len(heap) > k:
                heapq.heappop(heap)

        top_k = [nums for count, nums in heap]
        return top_k


        