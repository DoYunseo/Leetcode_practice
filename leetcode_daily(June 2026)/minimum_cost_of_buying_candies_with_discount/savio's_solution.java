class Solution {
    public int minimumCost(int[] cost) {
        Arrays.sort(cost);
        int n = cost.length;
        int result = 0;
        // this is the cheapest in its group of 3m
        for (int i = n - 1; i >= 0; i--) {
            if ((n - 1 - i) % 3 == 2)
                continue;
            result += cost[i];
        }
        return result;
    }
}