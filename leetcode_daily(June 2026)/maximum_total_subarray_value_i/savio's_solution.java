class Solution {
    public long maxTotalValue(int[] nums, int k) {
        long result = 0;
        long mini = Arrays.stream(nums).min().getAsInt();
        long maxi = Arrays.stream(nums).max().getAsInt();
        result = (maxi - mini) * k;
        return result;
    }
}