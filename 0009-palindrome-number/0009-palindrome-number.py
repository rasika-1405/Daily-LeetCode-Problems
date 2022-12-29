class Solution:
    def isPalindrome(self, x: int) -> bool:
        # check if integer is negative - return false
        if x < 0:
            return False
        elif x==0:
            return True
        
        # convert x into string
        x_str = str(x)
        
        # check len(string) - odd or even?
        x_len = len(x_str)
         # initialize 2 pointers - start and end
        start = 0
        end = x_len-1
        
        # iterate over the string
        # check if character at start and end are equal
        # if not -> return false
        # until start = end -> return true
        if x_len % 2 == 0: # even
            while end != start-1:
                if x_str[start] != x_str[end]:
                    return False
                start += 1
                end -= 1
        else: # odd
            while start != end:
                if x_str[start] != x_str[end]:
                    return False
                start += 1
                end -= 1
                
        return True    
        # 1, 2, 3, 4
        #.   s, e
        #.   e, s