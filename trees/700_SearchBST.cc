#include <iostream>

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
    TreeNode* searchBST(TreeNode* root, int val) {
        TreeNode* target = search(root, val);
        return target;
    }

    TreeNode* search(TreeNode* node, int val){
        if(!node) return nullptr;
        if(node->val > val){
            return search(node->left, val);
        }
        else if(node->val < val){
            return search(node->right, val);
        }
        else{
            return node;
        }
    }
};