class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        answer = []
        while left < right:
            goal = target - numbers[left]
            while numbers[right] >= goal:
                if numbers[right] == goal:
                    left += 1
                    right += 1
                    answer.append(left)
                    answer.append(right)
                    return answer
                right -= 1
            left += 1
