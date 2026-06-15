class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        fresh = 0
        time = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in direction:
                    udr, udc = row + dr, col + dc
                    if udr < 0 or udc < 0 or udr >= ROW or udc >= COL or grid[udr][udc] != 1:
                        continue
                    grid[udr][udc] = 2
                    q.append((udr, udc))
                    fresh -= 1
            time += 1

        return time if not fresh else -1