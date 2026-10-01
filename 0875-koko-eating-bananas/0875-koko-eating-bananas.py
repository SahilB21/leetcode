class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        best = right
        while left < right:
            pace = (left+right) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/pace)
            if hours > h:
                left = pace + 1
            else:
                best = pace
                right = pace
        return best
