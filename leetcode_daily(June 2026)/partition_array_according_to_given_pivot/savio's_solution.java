class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        int count = 0;

        for (int num: nums) {
            if (num < pivot) left.add(num);
            if (num > pivot) right.add(num);
            if (num == pivot) count++;
        }
        System.out.println(left);
        int m = left.size();
        int n = right.size();
        List<Integer> result = new ArrayList<>();

        for(int item: left) {
            result.add(item);
        }

        for (int i = 0; i < count; i++) {
            result.add(pivot);
        }

        for (int item: right) {
            result.add(item);
        }

        return result.stream().mapToInt(Integer::intValue).toArray();

    }
}