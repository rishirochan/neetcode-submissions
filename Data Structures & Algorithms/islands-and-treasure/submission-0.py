class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROW, COL = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(r, c):
            q = deque([[r, c]])
            visit = [[False] * COL for i in range(ROW)]
            visit[r][c] = True
            step = 0
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return step
                    for dr, dc in directions:
                        udr, udc = row + dr, col + dc
                        if udr < 0 or udc < 0 or udr >= ROW or udc >= COL or grid[udr][udc] == -1 or visit[udr][udc]:
                            continue
                        visit[udr][udc] = True
                        q.append([udr, udc])
                step += 1
            return INF

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)