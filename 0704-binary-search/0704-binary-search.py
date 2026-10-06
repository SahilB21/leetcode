class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        final = -1
        while left <= right:
            index = int((left+right)/2)
            if nums[index] == target:
                final = index
                break
            elif target < nums[index]:
                right = index - 1
            else:
                left = index + 1
        return final

         