class Solution:
    def isPalindrome(self, x: int) -> bool:
        # check if integer is negative - return false
        # if x < 0:
        #     return False
        # elif x==0:
        #     return True
        
        # convert x into string
        # x_str = str(x)
        # rev_str = x_str[::-1]
        # return rev_str == x_str
        
        # check len(string) - odd or even?
         # initialize 2 pointers - start and end
#         start = 0
#         end = x_len-1

#         if x_len % 2 == 0: # even
#             while end != start-1:
#                 if x_str[start] != x_str[end]:
#                     return False
#                 start += 1
#                 end -= 1
#         else: # odd
#             while start != end:
#                 if x_str[start] != x_str[end]:
#                     return False
#                 start += 1
#                 end -= 1

        # rev_str = ""
        # for each in range(x_len-1, -1, -1):
        #     rev_str += x_str[each]
        
         # return str(x) == str(x)[::-1]
            
        """
        return if it is a negative integer
        initialize rev_number = 0
        while given_number > 0:
            unit_place of given_number
            multiply rev_num by 10
            add unit_place to rev_number
            divide given_number by 10
        check rev_number == given_number ?
        
        """    
        if x < 0:
            return False
        rev_num = 0
        given_num = x
        while x > 0:
            units_place = x % 10
            rev_num *= 10
            rev_num += units_place
            x = x // 10
        return given_num == rev_num
        