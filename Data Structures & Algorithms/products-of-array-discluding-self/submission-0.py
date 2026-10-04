class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        sufix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            sufix[i] = sufix[i + 1] * nums[i + 1]

        answer = []
        for i in range(len(nums) ):
            answer.append(prefix[i] * sufix[i])
        
        return answer
            