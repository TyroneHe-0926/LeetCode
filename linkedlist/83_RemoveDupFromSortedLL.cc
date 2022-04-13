struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *sentinel = new ListNode(-101, head);
        ListNode *prevnode = sentinel, *curnode = head;
        while(curnode){
            if(prevnode->val == curnode->val){
                ListNode *tempprev = curnode;
                curnode = curnode->next;
                prevnode->next = curnode;
                delete tempprev;
            }
            else{
                prevnode = prevnode->next;
                curnode = curnode->next;
            }
        }
        return head;
    }
};