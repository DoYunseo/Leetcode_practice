class Solution {
    public int minimumOperations(int[] nums) {
        int result = 0;
        for (int num : nums) {
            result += Math.min(num % 3, 3 - (num % 3));
        }
        return result;
    }
}