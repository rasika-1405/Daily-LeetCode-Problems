class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer,Integer> sumMap = new HashMap<>();
        
        for (int i=0;i<nums.length;i++){
            if(sumMap.containsKey(target-nums[i])){
                return new int[] {sumMap.get(target-nums[i]), i};
            } else {
                sumMap.put(nums[i], i);
            }
        }
        return new int[]{-1, -1};
    }
}