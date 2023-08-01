from typing import List
from copy import deepcopy

class Solution(object):

    result: List[List[int]]
    
    def __init__(self): self.result = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        cur_list = []
        self.combine_helper(0, n, k, cur_list)
        return self.result

    def combine_helper(self, cur_num, n, k, cur_list: List[int]):
        if k == 0:
            temp_list = deepcopy(cur_list)
            self.result.append(temp_list)
            return
        if cur_num == n: return
        self.combine_helper(cur_num+1, n, k, cur_list)
        cur_list.append(cur_num+1)
        self.combine_helper(cur_num+1, n, k-1, cur_list)
        cur_list.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.combine(4,2))

"""
class Solution {
public:
    vector<vector<int>> ans;
    void dfs(int i , int n , int k , vector<int>& temp){
        if(k == 0){
            ans.push_back(temp);
            return ;
        }
        if(i == n) return ;
        dfs(i + 1 , n , k , temp);
        temp.push_back(i+1);
        dfs(i + 1 , n , k - 1 , temp);
        temp.pop_back();
    }
    vector<vector<int>> combine(int n, int k) {
        vector<int> temp;
        dfs(0 , n , k , temp);
        return ans;
    }
};
"""