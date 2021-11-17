class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        for(int number = 0; number < nums.length; number++) {
            for(int index = number + 1; index < nums.length; index++) {
                if(nums[number] + nums[index] == target) {
                    result[0] = number;
                    result[1] = index;
                    return result;
                }
            }
        }
        return result;
    }
}