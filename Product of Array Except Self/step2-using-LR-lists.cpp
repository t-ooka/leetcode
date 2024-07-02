class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();
        
        vector<int> L(length);
        L[0] = 1;
        for (int i = 1; i < length; i++) {
            L[i] = L[i-1] * nums[i-1];
        }

        vector<int> R(length);
        R[length-1] = 1;
        for (int i = length-2; i >= 0; i--) {
            R[i] = R[i+1] * nums[i+1]; 
        }

        vector<int> ans(length);
        for (int i = 0; i < length; i++) {
            ans[i] = L[i] * R[i];
        }

        return ans;
    }
};
