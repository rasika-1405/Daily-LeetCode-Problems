class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> romInt = new HashMap<Character, Integer>();
        romInt.put('I', 1);
        romInt.put('V', 5);
        romInt.put('X', 10);
        romInt.put('L', 50);
        romInt.put('C', 100);
        romInt.put('D', 500);
        romInt.put('M', 1000);
        
        int n = s.length();
        int intValue=0;
        
        for (int i=0; i<n-1; i++){
            if (romInt.get(s.charAt(i)) >= romInt.get(s.charAt(i+1))){
                intValue += romInt.get(s.charAt(i));
            } else{
                intValue -= romInt.get(s.charAt(i));
            }
        }
        intValue += romInt.get(s.charAt(n-1));
        return intValue;
    }
}