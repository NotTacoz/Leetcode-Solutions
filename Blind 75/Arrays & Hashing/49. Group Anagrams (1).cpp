// 28/11/24

class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        vector<vector<string>> v = {};

        unordered_map<string, vector<string>> seen;
        for (int i = 0; i < strs.size(); i++)
        {
            string x = strs[i];
            sort(x.begin(), x.end());
            seen[x].push_back(strs[i]);
        }

        for (auto &i : seen)
        {
            v.push_back(i.second);
            // copy(i.begin(),i.end(),ostream_iterator<string>)
        }
        return v;
    }
};