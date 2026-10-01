class Solution {
    public int climb(int i, int[] cost, Integer[] dp) {
        if (i >= cost.length)
            return 0;
        if (dp[i] != null)
            return dp[i];
        int one = climb(i + 1, cost, dp);
        int two = climb(i + 2, cost, dp);
        dp[i] = cost[i] + Math.min(one, two);
        return dp[i];

    }

    public int minCostClimbingStairs(int[] cost) {
        Integer[] dp = new Integer[cost.length];
        return Math.min(climb(0, cost, dp), climb(1, cost, dp));
    }
}