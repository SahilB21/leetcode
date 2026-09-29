class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []
        ans = [-1] * len(nums)
        for i in range(2 * len(nums)):
            while stack and nums[i % len(nums)] > nums[stack[-1]]:
                popped = stack.pop()
                ans[popped] = nums[i % len(nums)]
            stack.append(i % len(nums))
        return ans