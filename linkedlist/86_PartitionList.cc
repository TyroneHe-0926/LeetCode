#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    void printList(ListNode* head){
        for(ListNode* curnode = head; curnode; curnode=curnode->next){
            cout<<curnode->val<<" ";
        }
        cout<<endl;
    }

    ListNode* partition(ListNode* head, int x) {
        if(!head){return nullptr;}
        if(!head->next){return head;}
        
        ListNode* head1 = new ListNode{};
        ListNode* head2 = new ListNode{};

        ListNode* temp1 = head1, *temp2 = head2;

        // keep track of the last previous node, for joining purposes later on.
        ListNode* prev1 = temp1, *prev2 = temp2;

        // construct list which contains all numbers < x
        // and another list which contains all numbers >= x
        for(ListNode* curnode = head; curnode != nullptr; curnode=curnode->next){
            if(curnode->val < x){
                temp1->val = curnode->val;
                prev1 = temp1;
                temp1->next = new ListNode{};
                temp1 = temp1->next;
            }
            if(curnode->val >= x){
                temp2->val = curnode->val;
                prev2 = temp2;
                temp2->next = new ListNode{};
                temp2 = temp2->next;
            }
        }
        
        //if all numbers are >= x, take only list2
        if(!head1 -> next ){
            prev2->next = nullptr;
            return head2;
        }

        //if all numbers are < x, take only list1
        if(!head2->next){
            prev1->next = nullptr;
            return head1;
        }

        //join list
        prev2->next = nullptr;
        prev1->next = head2;

        return head1;
    }
};
