struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    int sum = 0;
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        this->traverse(root, low, high);
        return this->sum;
    }

    void traverse(TreeNode* node, int low, int high){
        if(node == nullptr) return;
        if(node->val <= high && node->val >= low){
            sum += node->val;
        }
        traverse(node->left, low, high);
        traverse(node->right, low, high);
    }
};