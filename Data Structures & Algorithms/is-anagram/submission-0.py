class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        count= {}

        for val in s:
            count[val] = count.get(val,0)+1
        
        for val in t: 
            if val not in count:
                return False
            
            count[val] -= 1

            if count[val]<0:
                return False
        
        return True


    