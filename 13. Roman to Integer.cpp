// 28/11/24
class Solution
{
public:
    int romanToInt(string s)
    {
        reverse(s.begin(), s.end());
        int x = 1;
        int y = 1;
        int z = 1;
        int v = 0;
        for (char j : s)
        {
            cout << j << " and the action done is ";
            if (j == 'I')
            {
                cout << "adding " << x << '\n';
                v = v + x;
                if (x == -1)
                {
                    x = 1;
                }
            }
            if (j == 'V')
            {
                v = v + 5;
                cout << "adding " << 5 << '\n';
                x = -1;
            }
            if (j == 'X')
            {
                cout << "adding " << 10 * y << '\n';
                v = v + 10 * y;
                x = -1;
                y = -1;
                if (y == -1)
                {
                    y = +1;
                }
            }
            if (j == 'L')
            {
                cout << "adding " << 50 << '\n';
                v = v + 50;
                y = -1;
            }
            if (j == 'C')
            {
                cout << "adding " << 100 * z << '\n';
                v = v + 100 * z;
                y = -1;
                if (z == -1)
                {
                    z = +1;
                }
            }
            if (j == 'D')
            {
                cout << "adding " << 500 << '\n';
                v = v + 500;
                z = -1;
            }
            if (j == 'M')
            {
                cout << "adding " << 1000 << '\n';
                v = v + 1000;
                z = -1;
            }
        }
        return v;
    }
};