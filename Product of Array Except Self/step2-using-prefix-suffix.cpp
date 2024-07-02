class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();
        vector<int> res(length);
        int prefix = 1;

        for (int i = 0; i < length; i++ ){
            res[i] = prefix;
            prefix *= nums[i];
        }

        int suffix = 1;

        for (int i = length-1; i >= 0; i--) {
            res[i] *= suffix;
            suffix *= nums[i];
        }

        return res;
    }
};
