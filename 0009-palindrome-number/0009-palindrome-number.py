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
        
        return str(x) == str(x)[::-1]
        
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