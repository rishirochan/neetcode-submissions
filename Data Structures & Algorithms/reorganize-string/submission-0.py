from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        h = []
        res = ""
        for key, val in c.items():
            heappush(h, (-1 * val, key))
        
        temp = None
        while h:
            val, key = heappop(h)
            if temp and temp[0] < 0:
                heappush(h, temp)
            temp = (val + 1, key)
            res += str(key)
        return res if temp[0] == 0 else ""