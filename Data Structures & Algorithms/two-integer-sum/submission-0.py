class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, element in enumerate(nums):
            search = target - element
            if search in d:
                return [d.get(search), index]
            d[element] = index