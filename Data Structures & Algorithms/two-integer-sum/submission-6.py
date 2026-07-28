class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}

        for i,n in enumerate(nums):
            second = target - n
            if second in map:
                return[map[second], i]
            map[n]=i