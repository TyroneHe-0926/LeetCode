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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(not root){
            root = new TreeNode(val);
        }
        else{
            insert(root, val);
        }
        return root;
    }

    void insert(TreeNode* root, int val){
        if(root->val < val){
            if(root->right){
                insert(root->right, val);
            }
            else{
                root->right = new TreeNode(val);
            }
        }
        if(root->val > val){
            if(root->left){
                insert(root->left, val);
            }
            else{
                root->left = new TreeNode(val);
            }
        }
    }
};