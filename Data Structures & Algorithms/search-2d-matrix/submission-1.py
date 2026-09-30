class Solution:
    def binarySearch(self, left: int, right: int, collums: List[int], target: int) -> int:
        if left > right:
            return -1

        middle = left + (right - left) // 2

        if collums[middle] == target:
            return middle
        
        if collums[middle] < target:
            left = middle + 1
            return self.binarySearch(left, right, collums, target)
        
        if collums[middle] > target:
            right = middle - 1
            return self.binarySearch(left, right, collums, target)
            
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        all = []
        for row in matrix:
            for cell in row:
                all.append(cell)
        
        return self.binarySearch(0, len(all) - 1, all, target) != -1