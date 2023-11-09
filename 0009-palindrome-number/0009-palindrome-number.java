class Solution {
    public boolean isPalindrome(int x) {
        int revNum = 0;
        int givenNum = x;
        
        while(x>0){
            int unitsNum = x % 10;
            revNum *= 10;
            revNum += unitsNum;
            x = x / 10;
        }
        if(givenNum == revNum) return true;
        return false;
    }
}