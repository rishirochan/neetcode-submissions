class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0

        # def dfs(r, c):
        #     if r < 0 or r >= ROW:
        #         return
        #     if c < 0 or c >= COL:
        #         return
        #     if grid[r][c] == '0':
        #         return
            
        #     grid[r][c] = '0'
        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc)

        def bfs(r, c):
            grid[r][c] = '0'
            q = deque([[r,c]])

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    udr, udc = r + dr, c + dc
                    if udr < 0 or udr >= ROW:
                        continue
                    if udc < 0 or udc >= COL:
                        continue
                    if grid[udr][udc] == '0':
                        continue
                    q.append([udr, udc])
                    grid[udr][udc] = '0'
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1':
                    #dfs(i, j)
                    bfs(i, j)
                    res += 1
        return res
