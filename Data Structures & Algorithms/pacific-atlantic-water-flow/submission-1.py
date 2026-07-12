class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pac, alt = set(), set()

        def dfs(r, c, visit, previous):
            if r < 0 or r >= ROW or c < 0 or c >= COL or heights[r][c] < previous or (r,c) in visit:
                return
            
            visit.add((r,c))
            for ur, uc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + ur, c + uc, visit, heights[r][c])            


        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL - 1, alt, heights[r][COL - 1])

        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW - 1, c, alt, heights[ROW - 1][c])

        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pac and (r, c) in alt:
                    res.append([r, c])
        return res