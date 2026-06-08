class Solution {
    public int[] leftRightDifference(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];

        int[] prefix = new int[n];
        int[] suffix = new int[n];
        
        prefix[0] = 0;
        suffix[n - 1] = 0;

        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] + nums[i - 1];
        }

        for (int i = n - 2; i >= 0; i--) {
            suffix[i] = suffix[i + 1] + nums[i + 1];
        }

        for (int i = 0; i < n; i++) {
            ans[i] = Math.abs(suffix[i] - prefix[i]);
        }

        return ans;
    }
}