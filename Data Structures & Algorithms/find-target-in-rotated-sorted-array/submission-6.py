class Solution:
    def findPivot(self, left, right, nums) -> int:
        l = left
        r = right

        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return l

    def binarySearch(self, left, right, target, nums) -> int:
        l, r = left, right

        if l > r:
            return -1

        m = l + (r - l) // 2

        if nums[m] == target:
            return m
        elif target > nums[m]:
            return self.binarySearch(m + 1, r, target, nums)
        
        else:
            return self.binarySearch(l, m - 1, target, nums)
            
        

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        pivot = self.findPivot(left, right, nums)
        if pivot == 0:
            return self.binarySearch(left, right, target, nums)
        if target >= nums[0]:
            return self.binarySearch(0, pivot - 1, target, nums)

        else:
            return self.binarySearch(pivot, right, target, nums)        




