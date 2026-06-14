class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = '0'
            q.append([r, c])

            while q:
                row, col = q.popleft()
                for ur, uc in directions:
                    udr, udc = row + ur, col + uc
                    if udr < 0 or udc < 0 or udr >= ROWS or udc >= COLS or grid[udr][udc] == '0':
                        continue
                    q.append([udr, udc])
                    grid[udr][udc] = '0'
        
        for rw in range(ROWS):
            for cls in range(COLS):
                if grid[rw][cls] == '1':
                    bfs(rw, cls)
                    islands += 1
        return islands