#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class BSTIterator {
public:
    vector<int> values;
    int pointer = 0;
    BSTIterator(TreeNode* root) {
        this->values.push_back(-1);
        this->inOrderTraverse(root);
    }
    
    int next() {
        this->pointer++;
        return this->values[this->pointer];
    }
    
    bool hasNext() {
        return this->pointer+1 >= values.size();
    }

    void inOrderTraverse(TreeNode* node){
        if(node && node->left) this->inOrderTraverse(node->left);
        if(node) this->values.push_back(node->val);
        if(node && node->right) this->inOrderTraverse(node->right);
    }
};