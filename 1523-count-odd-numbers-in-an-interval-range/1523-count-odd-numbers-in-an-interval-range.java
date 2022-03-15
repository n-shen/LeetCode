class Solution {
    public int countOdds(int low, int high) {
        int num = 0;
        if (high % 2 == 0 && low % 2 == 0) {
            num = (high - low) / 2;
        } else {
            num = (high - low) / 2 + 1;
        }
        return num;
    }
}