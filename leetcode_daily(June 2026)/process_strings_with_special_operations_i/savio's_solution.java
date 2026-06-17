class Solution {
    public String processStr(String s) {
        StringBuilder running = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '*') {
                if (running.length() < 1) {
                continue;
            }
                running.deleteCharAt(running.length() - 1);
            }
            else if (s.charAt(i) == '#') {
                StringBuilder duplicate = new StringBuilder(running.toString());
                running.append(duplicate);
            }
            else if (s.charAt(i) == '%') {
                running.reverse();
                continue;
            }
            else {
                running.append(s.charAt(i));
            }
        }
        return running.toString();
    }
}