class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = nums[:]
        rightProduct = 1
        final[0] = 1
        for i in range(1, len(nums)):
            final[i] = nums[i-1] * final[i-1]
        for i in range(len(nums) - 1, -1, -1):
            final[i] *= rightProduct
            rightProduct *= nums[i]
        return final