class Solution {
    public int totalWaviness(int num1, int num2) {
        int totalWaviness = 0;
        for (int i = num1; i <= num2; i++) {
            int wavy = 0;
            char [] digits = String.valueOf(i).toCharArray();
            int n = digits.length;

            if (n < 3) {
                totalWaviness += wavy;
                continue;
            }

            for (int j = 1; j < digits.length - 1; j++) {
                if (digits[j] > digits[j - 1] && digits[j] > digits[j + 1]) {
                    wavy += 1;
                }
                else if (digits[j] < digits[j - 1] && digits[j] < digits[j + 1]) {
                    wavy += 1;
                }
            }
            totalWaviness += wavy;
        }
        return totalWaviness;
    }
}