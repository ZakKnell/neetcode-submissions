class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        valid = seen.keys()

        longest = 1
        for key in valid:
            if key - 1 not in valid:
                current_length = 1
                current = key
                while current + 1 in valid:
                    current_length += 1
                    current = current + 1
                if current_length > longest:
                    longest = current_length
        
        return longest
                    
