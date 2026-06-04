
class Solution {
    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int n = landStartTime.length;
        int m = waterStartTime.length;
        int[] landFinishTimes = new int[n];
        int[] waterFinishTimes = new int[m];

        for (int i = 0; i < n; i++) {
            landFinishTimes[i] = landStartTime[i] + landDuration[i];
        }

        for (int i = 0; i < m; i++) {
            waterFinishTimes[i] = waterStartTime[i] + waterDuration[i];
        }

        int minLand = java.util.Arrays.stream(landFinishTimes).min().getAsInt();
        int minWater = java.util.Arrays.stream(waterFinishTimes).min().getAsInt();

        int earliest_time_i = Integer.MAX_VALUE;
        int earliest_time_ii = Integer.MAX_VALUE;

        for (int i = 0; i < m; i++) {
            earliest_time_i = Math.min(earliest_time_i, Math.max(minLand, waterStartTime[i]) + waterDuration[i]);
        }

        for (int i = 0; i < n; i++) {
            earliest_time_ii = Math.min(earliest_time_ii, Math.max(minWater, landStartTime[i]) + landDuration[i]);
        }

        return Math.min(earliest_time_i, earliest_time_ii);
    }
}