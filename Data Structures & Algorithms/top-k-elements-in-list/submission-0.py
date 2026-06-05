from heapq import heapify, heappush, heappop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        h = [(-count, key) for key, count in freq.items()]
        heapify(h)
        i=0
        ans = []

        while i < k:
            ans.append(heappop(h)[1])
            i += 1
        
        return ans