import java.util.*;

class Solution {
    public int findLucky(int[] arr) {
        HashMap<Integer, Integer> hmap = new HashMap<>();

        for(int i = 0; i < arr.length; i++) {
            if (hmap.get(arr[i]) == null) {
                hmap.put(arr[i], 1);
            }
            else {
                hmap.put(arr[i], hmap.get(arr[i]) + 1);
            }
           
        }
        int maxi = -1;
        for (Map.Entry<Integer, Integer> entry: hmap.entrySet()) {
            if(entry.getKey() == entry.getValue()) {
                maxi = Math.max(maxi, entry.getKey());
            }
        }
        return maxi;
    }
}