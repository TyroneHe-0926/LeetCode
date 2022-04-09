#include <vector>
#include <map>

using namespace std;

class Solution {
public:
  int oddEvenJumps(vector<int>& A) {
    const int n = A.size();
    map<int, int> m;
    vector<vector<int>> dp(n + 1, vector<int>(2));
    dp[n - 1][0] = dp[n - 1][1] = 1;
    m[A[n - 1]] = n - 1;
    int ans = 1;
    for (int i = n - 2; i >= 0; --i) {
      auto o = m.lower_bound(A[i]);
      if (o != m.end()) dp[i][0] = dp[o->second][1];
      auto e = m.upper_bound(A[i]);
      if (e != m.begin()) dp[i][1] = dp[prev(e)->second][0];
      if (dp[i][0]) ++ans;
      m[A[i]] = i;
    }
    return ans;
  }
};