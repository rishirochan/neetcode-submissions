class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxheap = [-t for t in freq.values()]
        heapq.heapify(maxheap)
        q = deque()
        time = 0

        while q or maxheap:
            if maxheap:
                cnt = heapq.heappop(maxheap) + 1
                if cnt:
                    q.append([cnt, n + time])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
            time += 1
        
        return time