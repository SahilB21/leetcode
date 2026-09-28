class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while (len(stack) != 0) and (temperatures[i] > temperatures[stack[-1]]):
                popped = stack.pop()
                ans[popped] = i - popped
            stack.append(i)
        return ans