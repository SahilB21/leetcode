class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = dict()
        for i in range(len(nums)):
            numbers[nums[i]] = i
        print(numbers)
        indices = []
        for i in range(len(nums)):
            if target - nums[i] in numbers and i != numbers[(target-nums[i])]:
                indices = [i, numbers[(target-nums[i])]]
                return indices
            else:
                continue
        return indices
        