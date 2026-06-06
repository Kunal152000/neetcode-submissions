class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume_val = 0
        left = 0
        right = len(heights)-1
        while left<right:
            max_width = right - left
            max_water_height = min(heights[left],heights[right])
            max_volume = max_width*max_water_height      
            if max_volume > max_volume_val:
                max_volume_val = max_volume

            if heights[left] < heights[right]:
                left +=1
            else:
                right-=1



        return max_volume_val


        