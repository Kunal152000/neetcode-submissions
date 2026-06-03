class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        sort_val = sorted(set(nums))
        current = 1
        longest = 1
        for i in range(len(sort_val)):
            if sort_val[i-1]+1 == sort_val[i]:
                current = current+1
                longest = max(longest,current)
            else:
                current = 1
                continue
        print(max(current,longest))
        return longest

        