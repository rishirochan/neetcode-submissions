from heapq import heapify, heappush, heappop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        h = [(-count, key) for key, count in freq.items()]
        heapify(h)
        ans = []

        while k:
            ans.append(heappop(h)[1])
            k -= 1
        
        return ans