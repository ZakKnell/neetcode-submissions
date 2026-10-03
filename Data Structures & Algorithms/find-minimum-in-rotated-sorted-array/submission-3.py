class Solution:
    def binarySearch(self, l, r, nums) -> int:
        left = l
        right = r

        if nums[left] <= nums[right]:
            return nums[left]
        
        middle = left + (right - left) // 2

        if nums[middle] > nums[right]:
            return self.binarySearch(middle + 1, right, nums)
        
        else:
            return self.binarySearch(left, middle, nums)


    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        return self.binarySearch(l, r, nums)




        