class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            temp1 = -heapq.heappop(stones)
            temp2 = -heapq.heappop(stones)

            if temp1 - temp2 == 0:
                continue
            else:
                heapq.heappush(stones, -(temp1 - temp2))
        
        return -1 * stones[0] if stones else 0