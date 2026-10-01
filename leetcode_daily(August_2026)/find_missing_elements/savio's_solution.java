class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        Arrays.sort(nums);
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++)
            set.add(nums[i]);
        int first = nums[0], last = nums[nums.length - 1];
        List<Integer> result = new ArrayList<>();
        for (int i = first + 1; i <= last - 1; i++) {
            if (!set.contains(i))
                result.add(i);
        }
        return result;
    }
}