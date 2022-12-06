#include <unordered_map>

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
    ListNode* middleNode(ListNode* head) {
        int i = 0;
        unordered_map<int, ListNode*> nodeMap;
        ListNode* temp = head;
        while(temp != nullptr){
            nodeMap[i] = temp;
            temp = temp->next;
            ++i;
        }

        int mid = i/2;
        return nodeMap[mid];
    }
};