class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addItem(r,c):
            if (r < 0 or c < 0 or r >= ROW or c >= COL or (r, c) in visit or grid[r][c] == -1):
                return
            q.append([r,c])
            visit.add((r,c))

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addItem(r + 1, c)
                addItem(r - 1, c)
                addItem(r, c + 1)
                addItem(r, c - 1)
            dist += 1