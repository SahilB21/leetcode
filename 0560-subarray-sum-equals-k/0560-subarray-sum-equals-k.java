class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> prefixSums = new HashMap<>();
        int counter = 0;
        int sum = 0;
        prefixSums.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (prefixSums.containsKey(sum-k)) {
                counter += prefixSums.get(sum-k);
            }
            prefixSums.put(sum, prefixSums.getOrDefault(sum, 0) + 1);
        }
        return counter;
    }
}