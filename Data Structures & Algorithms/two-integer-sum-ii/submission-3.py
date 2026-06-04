class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        result = []
        while left < right:
            if numbers[right] + numbers[left] < target:     
                left = left+1
            elif numbers[right] + numbers[left] > target:
                right = right-1
            elif numbers[right] + numbers[left] == target: 
                result.append(left+1)
                result.append(right+1)
                return result

        # return result

        