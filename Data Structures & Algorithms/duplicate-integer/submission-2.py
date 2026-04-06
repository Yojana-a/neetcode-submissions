class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()

        for num in nums: #gothrough all numbers
            if num in seen:
                return True
            seen.add(num) #is 1 in seen No! then add, is 2 is seen No! then add, is 1 in seen Yes! then return True
        return False
        
