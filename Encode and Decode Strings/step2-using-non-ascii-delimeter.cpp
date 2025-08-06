class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string res = "";
        for (int i = 0; i < strs.size(); i++) {
            string str = strs[i];
            res += str + "あ";
        }
        return res;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> res;
        int pos = 0;
        while (pos < s.size()) {
            pos = s.find("あ");
            res.push_back(s.substr(0,pos));
            s.erase(0, pos+3);
        }
        return res;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));
