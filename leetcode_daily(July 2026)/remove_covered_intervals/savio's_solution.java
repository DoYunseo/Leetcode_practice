class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        // sort all the intervals by the first number
        int n = intervals.length;
        Arrays.sort(intervals, (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(b[1], a[1]));
        List<int[]> result = new ArrayList<>();
        result.add(intervals[0]);

        for (int i = 1; i < n; i++) {
            int[] lastAdded = result.get(result.size() - 1);
            if (intervals[i][0] <= lastAdded[1] && intervals[i][1] <= lastAdded[1])
                continue;
            result.add(intervals[i]);
        }
        return result.size();
    }
}