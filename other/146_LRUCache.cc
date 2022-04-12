#include <map>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class DLLNode{
public:
    DLLNode *prev;
    DLLNode *next;
    int val;
    int key;
    DLLNode(int key, int val){
        this->val = val;
        this->key = key;
        this->next = NULL;
        this->prev = NULL;
    }
};

class LRUCache {
public:
    int capacity;
    map<int, DLLNode*> m;
    DLLNode *head;
    DLLNode *tail;

    LRUCache(int capacity) {
        this->capacity = capacity;
        this->head = new DLLNode(-1, -1);
        this->tail = new DLLNode(-1, -1);
        this->head->next = this->tail;
        this->tail->prev = this->head;
    }

    int get(int key) {
        if(this->m.find(key) == this->m.end()){
            return -1;
        }
        else{
            this->moveNodeToEnd(key);
            return this->m.find(key)->second->val;
        }
    }

    void put(int key, int value) {
        if(this->m.find(key) == this->m.end()){
            if(this->capacity == this->m.size()){
                DLLNode* lrunode = this->head->next;
                int dkey = lrunode->key;
                this->m.erase(dkey);
                DLLNode* nexttemp = lrunode->next;
                this->head->next = nexttemp;
                nexttemp->prev = head;
                DLLNode* newnode = this->insert_node(key, value);
                this->m.insert({key, newnode});
                delete lrunode;
                return;
            }
            else{
                DLLNode* newnode = this->insert_node(key, value);
                this->m.insert({key, newnode});
            }
        }
        else{
            
            DLLNode* targetnode = this->m.find(key)->second;
            targetnode->val = value;
            this->moveNodeToEnd(key);
            this->m.find(key)->second->val = value;
        }
    }

    DLLNode* insert_node(int key, int value){
        DLLNode *newnode = new DLLNode(key, value);
        DLLNode *prevtemp = this->tail->prev;
        newnode->next = tail;
        newnode->prev = prevtemp;
        prevtemp->next = newnode;
        tail->prev = newnode;
        return newnode;
    }

    void moveNodeToEnd(int key){
        DLLNode* targetnode = this->m.find(key)->second;
        DLLNode *prevtemp = targetnode->prev;
        DLLNode *nexttemp = targetnode->next;
        prevtemp->next = nexttemp;
        nexttemp->prev = prevtemp;
        targetnode->next = this->tail;
        targetnode->prev = this->tail->prev;
        this->tail->prev->next = targetnode;
        this->tail->prev = targetnode;
    }

    void printList(){
        DLLNode *tempnode = this->head;
        while(tempnode){
            cout<<tempnode->val<<" ";
            tempnode = tempnode->next;
        }
        cout<<endl;
    }

    void printListReverse(){
        DLLNode *tempnode = this->tail;
        while(tempnode){
            cout<<tempnode->val<<" ";
            tempnode = tempnode->prev;
        }
        cout<<endl;
    }
};

int main(){
    LRUCache lRUCache = LRUCache(2);
    cout<<(lRUCache.get(2))<<endl;
    lRUCache.put(2,6);
    cout<<(lRUCache.get(1))<<endl;
    lRUCache.put(1,5);
    lRUCache.put(1,2);
    cout<<(lRUCache.get(1))<<endl;
    cout<<(lRUCache.get(2))<<endl;
}