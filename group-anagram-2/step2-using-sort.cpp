class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
      unordered_map<string, vector<string>> res;
      for (const auto& s : strs) {
        string sorted_string = s;
        sort(sorted_string.begin(), sorted_string.end());
        res[sorted_string].push_back(s);
      }
      vector<vector<string>> result;
      for (auto& pair : res) {
        result.push_back(pair.second);
      }
      return result;
    }
};
