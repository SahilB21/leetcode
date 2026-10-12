class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        seen = set([(0, 0)])
        t = 0
        while True:
            curr, x, y = heapq.heappop(pq)
            if curr >= t:
                t = curr
            if x == n - 1 and y == n - 1:
                return t
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= i < n and 0 <= j < n and (i, j) not in seen:
                    seen.add((i, j))
                    heapq.heappush(pq, (grid[i][j], i, j))


