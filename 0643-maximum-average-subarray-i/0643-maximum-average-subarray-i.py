class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        currSum = sum(nums[0:k])
        maxAvg = currSum / k
        while (len(nums) - 1 - i) >= k:
            currSum -= nums[i]
            currSum += nums[i+k]
            avg = currSum / k
            if (avg > maxAvg):
                maxAvg = avg
            i += 1
        return maxAvg
        
        