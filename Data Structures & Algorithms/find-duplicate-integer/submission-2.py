class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        loopLength = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]



            if slow == fast:
                while True:
                    slow = nums[slow]
                    fast = nums[nums[fast]]
                    loopLength += 1
                    if slow == fast:
                        break
                break

        p1 = nums[0] 
        p2 = nums[0]
        for i in range(loopLength):
            p2 = nums[p2]
        
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        
        return p1
        
