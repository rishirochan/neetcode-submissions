class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        visit = set()

        def additem(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or (r,c) in visit or grid[r][c] == -1:
                return
            
            q.append((r,c))
            visit.add((r,c))

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for ur, uc in directions:
                    additem(ur + r, uc + c)
            dist += 1

