#include <iostream>
#include <map>
#include <vector>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
    vector<Node*> nodes;
    vector<int> randompointers;
    map<Node*, int> nodemap;
    vector<Node*> newnodes;
    public:
        Node* copyRandomList(Node* head) {
            if(!head) return nullptr;
            Node *curnode = head;
            int curindex = 0;
            while(curnode){
                this->nodes.push_back(curnode);
                this->nodemap.insert({curnode, curindex});
                curnode = curnode->next;
                curindex ++;
            }
            curnode = head;
            while(curnode){
                if(!curnode->random) this->randompointers.push_back(-1);
                else{
                    this->randompointers.push_back(this->nodemap.find(curnode->random)->second);
                }
                curnode = curnode->next;
            }
            Node *newhead = new Node(this->nodes[0]->val);
            Node *newcur = newhead;
            for(int i = 1; i < this->nodes.size(); i++){
                Node* newnode = new Node(this->nodes[i]->val);
                newcur->next = newnode;
                this->newnodes.push_back(newcur);
                newcur = newcur->next;
            }
            this->newnodes.push_back(newcur);
            newcur = newhead;
            for(int i = 0; i < this->randompointers.size(); i++){
                int rdindex = this->randompointers[i];
                if(rdindex == -1){
                    newcur->random = nullptr;
                }
                else{
                    newcur->random = this->newnodes[rdindex];
                }
                newcur = newcur->next;
            }
            return newhead;
        }
};