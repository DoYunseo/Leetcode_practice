class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        double maxi = Double.MIN_VALUE;
        int result = 0;
        for (int[] item : dimensions) {
            double pyg = Math.sqrt((item[0] * item[0]) + (item[1] * item[1]));
            if (pyg > maxi) {
                pyg = maxi;
                result = item[0] * item[1];
            }
        }
        return result;
    }
}
