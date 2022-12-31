class Solution:
    def romanToInt(self, s: str) -> int:
        # IIV - invalid 
        """
        create a dictionary
        len of string
        iterate over string from right to left
        if value of left_character > value of right_character : add to sum
        else : subtract from sum
        """
        rom_int = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, 
                   "D" : 500, "M" : 1000}
        str_len = len(s)
        int_value = rom_int[s[str_len-1]]
        
        for i in range(str_len - 2, -1, -1):
            if rom_int[s[i]] >= rom_int[s[i+1]]:
                int_value += rom_int[s[i]]
            else:
                int_value -= rom_int[s[i]]
        
        return int_value
        