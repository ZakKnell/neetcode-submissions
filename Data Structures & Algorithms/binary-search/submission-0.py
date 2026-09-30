class Solution:
    def binarySearch(self, left: int, right: int, nums: List[int], target: int) -> int:

        if left > right:
            return -1

        middle = left + (right - left) // 2
        if nums[middle] == target:
            return middle
        
        if nums[middle] < target:
            left = middle + 1
            return self.binarySearch(left, right, nums, target)
        
        else:
            right = middle- 1
            return self.binarySearch(left, right, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums) - 1, nums, target)
