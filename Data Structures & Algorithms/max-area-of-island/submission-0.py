class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1, 0], [0,1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])
        islandsizes = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1
            for ur, uc in directions:
                udr, udc = r + ur, c + uc
                area += dfs(udr, udc)
            return area
        
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    val = dfs(row, col)
                    islandsizes = max(islandsizes, val)
        return islandsizes