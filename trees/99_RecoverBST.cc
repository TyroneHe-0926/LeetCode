#include <vector>
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

//O(n) space solution
class Solution {
public:
    vector<TreeNode*> nodes;
    void recoverTree(TreeNode* root) {
        this->inOrderTraverse(root);
        int dip1 = -1, dip2 = -1;
        for(int i = 0; i < this->nodes.size(); i++){
            if(i + 1 < this->nodes.size() && this->nodes[i+1]->val < this->nodes[i]->val){
                if(dip1 != -1){
                    dip2 = i+1;
                }
                else{
                    dip1 = i;
                }
            }
        }
        if(dip2 != -1){
            int val1 = nodes[dip1]->val,val2 = nodes[dip2]->val;
            nodes[dip1]->val = val2;
            nodes[dip2]->val = val1;
        }
        else{
            int val1 = nodes[dip1]->val,val2 = nodes[dip1+1]->val;
            nodes[dip1]->val = val2;
            nodes[dip1+1]->val = val1;
        }
    }

    void inOrderTraverse(TreeNode* node){
        if(node && node->left) this->inOrderTraverse(node->left);
        if(node) this->nodes.push_back(node);
        if(node && node->right) this->inOrderTraverse(node->right);
    }
};