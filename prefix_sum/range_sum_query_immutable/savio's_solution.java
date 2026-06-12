class NumArray {
    private int[] res;

    public NumArray(int[] nums) {
        int n = nums.length;
        res = new int[n + 1];
        for(int i = 1; i <= n; i++) {
            res[i] = res[i - 1] + nums[i - 1];
        }
    }
    
    public int sumRange(int left, int right) {
        return res[right + 1] - res[left];

    }
}
