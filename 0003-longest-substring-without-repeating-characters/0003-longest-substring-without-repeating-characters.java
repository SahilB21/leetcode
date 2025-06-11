class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longestSet = 0;
        for (int i = 0; i < s.length(); i++) {
            Set<String> substrings = new HashSet<String>();
            for (int j = i; j < s.length(); j++) {
                if (!substrings.contains(s.substring(j, j+1))) {
                    substrings.add(s.substring(j, j+1));
                    substrings.add(s.substring(i, j+1));
                } else {
                    break;
                }
            }

            for (String substring : substrings) {
                if (substring.length() > longestSet) {
                    longestSet = substring.length();
                }
            }
        }
        return longestSet;
    }
}