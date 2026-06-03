class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True
        # rev_string = ""
        # remove_space = s.replace(" ","")
        # remove_special= ""
        # for char in range(len(remove_space)):
        #     if remove_space[char].isalnum():
        #         remove_special = remove_special + remove_space[char]     
        #     else:
        #         continue

        # for char in range(len(remove_space)-1,-1,-1):
        #     if remove_space[char].isalnum():
        #         rev_string = rev_string + remove_space[char]     
        #     else:
        #         continue
        # # print(remove_special.lower(),rev_string.lower())
        # if remove_special.lower() ==  rev_string.lower():
        #     return True
        # else:
        #     return False
        left = 0
        right = len(s)-1

        while left < right:
            if not s[left].isalnum():
                left = left+1
            elif not s[right].isalnum():
                right = right -1
            elif s[left].lower() == s[right].lower():
                left = left+1
                right = right-1
                continue
            else:
                return False
            
            
        return True



        