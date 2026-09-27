class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        currentmax = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            if area > currentmax:
                currentmax = area
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return currentmax