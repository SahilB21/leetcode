class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max = 0
        while left < right:
            lower = left
            if height[left] > height[right]:
                lower = right
            curr = height[lower] * (right - left)
            if curr > max:
                max = curr
            if lower == left:
                left += 1
            else:
                right -= 1
        return max

