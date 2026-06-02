class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # K most frequent means; count of numbers which are repeated frequently
        frequent_dict = {}
        for num in nums:
            frequent_dict[num] = frequent_dict.get(num,0)+1
        
        top_k = []
        for key, value in sorted(frequent_dict.items(),key=lambda x: x[1], reverse=True):
                top_k.append(key)
            
        
        return top_k[:k]
            
            


        