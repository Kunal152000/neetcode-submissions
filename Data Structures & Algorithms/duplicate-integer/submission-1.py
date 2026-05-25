class Solution:
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     for i in range(0, len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             if nums[i]==nums[j]:
    #                 return True

    #     return False 
      def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        
        return False
            