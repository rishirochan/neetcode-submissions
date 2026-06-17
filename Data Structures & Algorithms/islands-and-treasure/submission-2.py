class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def addItem(r, c):
            if r < 0 or r >= ROW:
                return
            if c < 0 or c >= COL:
                return
            if grid[r][c] == -1:
                return
            if (r,c) in visit:
                return
            
            visit.add((r, c))
            q.append((r, c))

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                
                addItem(r - 1, c)
                addItem(r + 1, c)
                addItem(r, c - 1)
                addItem(r, c + 1)

            dist += 1
