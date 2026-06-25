class MedianFinder:

    def __init__(self):
        self.smallnum, self.largenum = [], []

    def addNum(self, num: int) -> None:
        if self.largenum and num > self.largenum[0]:
            heapq.heappush(self.largenum, num)
        else:
            heapq.heappush(self.smallnum, -num)
        
        if len(self.smallnum) > len(self.largenum) + 1:
            val = -1 * heapq.heappop(self.smallnum)
            heapq.heappush(self.largenum, val)
        if len(self.largenum) > len(self.smallnum) + 1:
            val = heapq.heappop(self.largenum)
            heapq.heappush(self.smallnum, -val)

    def findMedian(self) -> float:
        if len(self.smallnum) > len(self.largenum):
            return -1 * self.smallnum[0]
        elif len(self.largenum) > len(self.smallnum):
            return self.largenum[0]
        return (-1 * self.smallnum[0] + self.largenum[0]) / 2.0
        