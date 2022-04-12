#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

//gonna use the parent node shenanigans, and then run a bfs starting from the target node
class Solution {
    map<TreeNode*, TreeNode*> parent;
    set<TreeNode*> seen;
    public:
        vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
            vector<int> values;
            this->dfs(root);
            queue<pair<TreeNode*, int>> curqueue;
            curqueue.push({target, 0});
            seen.insert(target);

            while(!curqueue.empty()){
                pair<TreeNode*, int> cur = curqueue.front();
                TreeNode *curnode = cur.first;
                    if(cur.second == k){
                        values.push_back(curnode->val);
                    }
                    if(curnode->left and seen.find(curnode->left) == seen.end()){
                        seen.insert(curnode->left);
                        curqueue.push({curnode->left, cur.second+1});
                    }
                    if(curnode->right and seen.find(curnode->right) == seen.end()){
                        seen.insert(curnode->right);
                        curqueue.push({curnode->right, cur.second+1});
                    }
                    if(this->parent.find(curnode) != this->parent.end()){
                        TreeNode *p = this->parent.find(curnode)->second;
                        if(seen.find(p) == seen.end()){
                            seen.insert(p);
                            curqueue.push({p, cur.second+1});
                        }
                    }
                curqueue.pop();
            }
            return values;
        }

        void dfs(TreeNode* node, TreeNode* par = NULL){
            this->parent.insert({node, par});
            if(node->right){
                this->dfs(node->right, node);
            }
            if(node->left){
                this->dfs(node->left, node);
            }
        }
    };

int main(){
    Solution *solution = new Solution();
    TreeNode *root = new TreeNode(3);
    root->left = new TreeNode(5);
    root->left->left = new TreeNode(6);
    root->left->right = new TreeNode(2);
    root->left->right->left = new TreeNode(7);
    root->left->right->right = new TreeNode(4);
    root->right = new TreeNode(1);
    root->right->left = new TreeNode(0);
    root->right->right = new TreeNode(8);
    solution->distanceK(root, root->left, 2);
}