import math
class Solution:
    def checkValid(self, k: int, piles: List[int], h: int) -> bool:
        total = 0
        for pile in piles:
            total += math.ceil(pile / k)
        if total <= h:
            return True
        return False

    def binarySearch(self, left: int, right: int, piles: List[int], h: int) -> int:
        
        if left > right:
            return left

        k = left + (right - left) // 2
        if self.checkValid(k, piles, h):
            right = k - 1
            return self.binarySearch(left, right, piles, h)
        
        else:
            left = k + 1
            return self.binarySearch(left, right, piles, h)
        

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.binarySearch(1, max(piles), piles, h)


