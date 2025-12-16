class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
      unordered_map<string, vector<string>> mp;

      for (const string& s : strs) {
        array<int, 26> count{};
        count.fill(0);

        for (char c : s) {
          count[c - 'a']++;
        }

        string key;
        
        for (int num : count) {
          key += to_string(num);
          key += '#';
        }

        mp[key].push_back(s);
      }

      vector<vector<string>> result;
      result.reserve(mp.size());

      for (auto& [key, group] : mp) {
        result.push_back(std::move(group));
      }
      
      return result;
    }
};
