class Solution {
    public int findFinalValue(int[] nums, int original) {
        Set<Integer> mset = new HashSet<>();
        for (int num : nums) {
            mset.add(num);
        }
        while (mset.contains(original)) {
            original = original * 2;
        }
        return original;
    }
}