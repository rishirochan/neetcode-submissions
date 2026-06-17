class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0

        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                udr, udc = r + dr, c + dc
                area += dfs(udr, udc)
            return area
        
        for r in range(ROW):
            for c in range(COL):
                res = max(res, dfs(r, c))
        
        return res
        
