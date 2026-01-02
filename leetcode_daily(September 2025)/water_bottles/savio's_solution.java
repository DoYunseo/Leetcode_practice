class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int store = numBottles;
        int result = numBottles;

        while (store >= numExchange) {
            int newBottles = store / numExchange;
            result += newBottles;
            store = store % numExchange + newBottles;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int result = sol.numWaterBottles(15, 4);
        System.out.println(result);
    }
}
