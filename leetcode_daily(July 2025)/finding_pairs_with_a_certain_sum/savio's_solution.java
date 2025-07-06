import java.util.HashMap;

class FindSumPairs {
    
    private int[] nums1;
    private int[] nums2;

    private HashMap<Integer, Integer> freqMap;

    public FindSumPairs(int[] nums1, int[] nums2) {
        this.nums1 = nums1;
        this.nums2 = nums2;
        this.freqMap = new HashMap<>();

        for (int num : nums2) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

    }
    
    public void add(int index, int val) {

        int oldVal = this.nums2[index];

        freqMap.put(oldVal, freqMap.get(oldVal) - 1);
        
        this.nums2[index] += val;

        int newVal = this.nums2[index];

        freqMap.put(newVal, freqMap.getOrDefault(newVal, 0) + 1);
    }
    
    public int count(int tot) {
        int track = 0;
         for (int num1 : this.nums1) {
            int target = tot - num1;
            track += freqMap.getOrDefault(target, 0);
        }
        return track;
    }
}
