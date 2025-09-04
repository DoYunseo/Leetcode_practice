class Solution {
    public int findClosest(int x, int y, int z) {
        int dist_x = Math.abs(x - z);
        int dist_y = Math.abs(y - z);

        if (dist_x == dist_y) {
            return 0;
        }

        else if (dist_y > dist_x) {
            return 1;
        }
        
        return 2;
    }
}