class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([(0, 0, k, 0)])
        seen = set()

        while q:
            x, y, left, steps = q.popleft()
            if (x, y, left) in seen or left < 0:
                continue
            if x == m-1 and y == n-1:
                return steps
            seen.add((x, y, left))
            if grid[x][y] == 1:
                left -= 1
            if x + 1 < m:
                q.append((x+1, y, left, steps+1))
            if x - 1 >= 0:
                q.append((x-1, y, left, steps+1))
            if y + 1 < n:
                q.append((x, y+1, left, steps+1))
            if y - 1 >= 0:
                q.append((x, y-1, left, steps+1))
        return -1