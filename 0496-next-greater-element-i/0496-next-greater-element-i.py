class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        dictionary = {}
        ans = [-1] * len(nums1)
        for i in range(len(nums2)):
            while len(stack) != 0 and nums2[i] > stack[-1]:
                popped = stack.pop()
                dictionary[popped] = nums2[i]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            ans[i] = dictionary.get(nums1[i], -1)
        return ans

