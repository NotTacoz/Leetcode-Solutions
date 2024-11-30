class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        unordered_map<char, int> charCount;
        for (char n : s)
        {
            charCount[n]++;
        }
        for (char g : t)
        {
            charCount[g]--;
        }

        for (auto x : charCount)
        {
            if (x.second != 0)
            {
                return false;
            }
        }

        return true;
    }
};