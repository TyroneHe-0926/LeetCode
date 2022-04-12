#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
 
class Solution {
public:
    int result;
    vector<int> values;
    int closestValue(TreeNode* root, double target) {
        values.clear();
        this->inOrder(root);
        double minm = numeric_limits<int>::max();
        int index = 0;
        for(int i = 0; i < this->values.size(); i++){
            double diff = abs(target - this->values[i]);
            if(diff < minm){
                minm = diff;
                index = i;
            }
        }
        return this->values[index];
    }

    void inOrder(TreeNode *root){
        if(!root->left && !root->right){
            this->values.push_back(root->val);
            return;
        }
        if(root->left){
            this->inOrder(root->left);
        }
        this->values.push_back(root->val);
        if(root->right){
            this->inOrder(root->right);
        }
    }

    void printTree(TreeNode *root){
        this->inOrder(root);
        for (auto i: this->values) std::cout << i << ' ';
    }
};

int main(){
    struct TreeNode root(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(5));
    Solution solution = Solution();
    cout<<solution.closestValue(&root, 3.714286)<<endl;
}