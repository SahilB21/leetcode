class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = set()
        for number in nums:
            if number not in freq:
                freq.add(number)
            else:
                return True
        return False    
