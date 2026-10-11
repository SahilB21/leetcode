class Solution:

    def __init__(self, w: list[int]):
        self.sums = [w[0]]
        for i in range(1, len(w)):
            self.sums.append(self.sums[i-1] + w[i])

        
    def pickIndex(self) -> int:
        num = random.random() * self.sums[-1]
        return bisect.bisect(self.sums, num)

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()