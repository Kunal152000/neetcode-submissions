class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, val in enumerate(nums):
            difference = target - val
            if difference in seen:
                return [seen[difference],index]
            else:
                seen[val] = index
        