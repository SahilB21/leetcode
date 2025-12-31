class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = dict()
        indices = []
        for i, num in enumerate(nums):
            if target - num in numbers:
                indices = [i, numbers[target-num]]
                return indices
            numbers[num] = i
        return indices
        