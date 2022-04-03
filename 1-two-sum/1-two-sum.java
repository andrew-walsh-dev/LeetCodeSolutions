import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seenValues = new HashMap<Integer, Integer>();
        int i = 0;
        for (int num : nums) {
            if (seenValues.get(target - num) != null) {
                return new int[] { i, seenValues.get(target - num) };
            }
            seenValues.put(num, i);
            i++;
        }
        return new int[] { -1, 1 };
    }
}