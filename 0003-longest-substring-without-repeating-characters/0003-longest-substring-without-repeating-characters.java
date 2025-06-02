class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        for (int i = 0; i < s.length(); i++) {
            String longestSubstring = "";
            for (int j = i; j < s.length(); j++) {
                if (!longestSubstring.contains(s.substring(j, j+1))) {
                    longestSubstring += s.substring(j, j+1);
                } else {
                    break;
                }
            }
            if (longestSubstring.length() > maxLength) {
                maxLength = longestSubstring.length();
            }
        }
        return maxLength;
    }
}