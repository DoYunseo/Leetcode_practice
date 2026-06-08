class Solution {
    int MOD = 1_000_000_007;

    private int[] prefixSum(int[] arr) {
        int n = arr.length;
        int[] new_arr = new int[n];
        new_arr[0] = arr[0];

        for (int i = 1; i < n; i++) {
            new_arr[i] = (new_arr[i - 1] + arr[i]) % MOD;
        }
        return new_arr;
    }

    public int valueAfterKSeconds(int n, int k) {
        int[] a = new int[n];
        Arrays.fill(a, 1);

        for (int i = 0; i < k; i++) {
            a = this.prefixSum(a);
        }
        return a[n - 1];
    }
}