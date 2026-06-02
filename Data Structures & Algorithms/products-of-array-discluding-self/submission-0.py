class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        val_arr = []
        
        for i in range(len(nums)):
            mult = 1
            for j in range(len(nums)):
                if j!=i:
                    mult = mult*nums[j]

            val_arr.append(mult)
        
        return val_arr



