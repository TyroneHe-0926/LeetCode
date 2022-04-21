#include <vector>
#include <iostream>
using namespace std;

/*
Different from the hashmap design one where i used just a simple LL
This one used mod hash bucket approach
*/
class LLNode{
    public:
        int val;
        LLNode* next;
        LLNode(int val){
            this->val = val;
            this->next = nullptr;
        }
};

class MyHashSet {
    int mod = 800;
    vector<LLNode*> buckets;
    public:
        MyHashSet() {
            for(int i = 0;i <= this->mod; i++){
                buckets.push_back(nullptr);
            }
        }
        
        void add(int key) {
            int target_bucket = key % this->mod;
            if(this->buckets[target_bucket]){
                LLNode* head = this->buckets[target_bucket];
                while(head && head->next){
                    if(head->val == key) return;
                    head = head->next;
                }
                if(head->val == key) return;
                else{
                    head->next = new LLNode(key);
                }
            }
            else{
                LLNode* head = new LLNode(key);
                this->buckets[target_bucket] = head;
            }
        }
        
        void remove(int key) {
            int target_bucket = key % this->mod;
            LLNode* head = this->buckets[target_bucket];
            LLNode* prev = nullptr;
            if(!head) return;
            if(head->val == key){
                this->buckets[target_bucket] = head->next;
                return;
            }
            while(head){
                if(head->val == key){
                    LLNode* next = head->next;
                    prev->next = next;
                    return;
                }
                prev = head;
                head = head->next;
            }
        }
        
        bool contains(int key) {
            int target_bucket = key % this->mod;
            if(!this->buckets[target_bucket]) return false;
            else{
                LLNode* head = this->buckets[target_bucket];
                while(head){
                    if(head->val == key){
                        return true;
                    }
                    head = head->next;
                }
            }
            return false;
        }
};

int main(){
    MyHashSet *myHashSet = new MyHashSet();
    myHashSet->add(2);      // set = [1, 2]
    cout<<myHashSet->contains(2)<<endl; // return True
    cout<<myHashSet->contains(1)<<endl; // return False
    myHashSet->add(1);      // set = [1, 2]
    cout<<myHashSet->contains(1)<<endl; // return True
    myHashSet->add(802);      // set = [1, 2]
    cout<<myHashSet->contains(802)<<endl; // return True
    myHashSet->remove(2);
    myHashSet->remove(88);
    cout<<myHashSet->contains(2)<<endl;
    cout<<myHashSet->contains(802)<<endl;
}