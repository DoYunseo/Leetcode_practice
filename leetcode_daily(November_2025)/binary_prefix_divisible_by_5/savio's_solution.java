class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        int sum = 0;
        List<Boolean> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            sum = (sum * 2 + (nums[i])) % 5;
            res.add(sum % 5 == 0);
        }
        return res;
    }
}