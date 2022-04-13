#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string minRemoveToMakeValid(string s) {
        vector<int> parens;
        int len = s.size();
        for(int i = 0; i < len; i++){
            if(s[i] == '('){
                parens.push_back(i);
            }
            else if(s[i] == ')' && parens.empty()){
                s[i] = ' ';
            }
            else if(s[i] == ')' && !parens.empty()){
                parens.pop_back();
            }
        }
        for(int i : parens) s[i] = ' ';
        s.erase(remove(s.begin(), s.end(), ' '), s.end());
        return s;
    }
};

// LC saids we could also do a too pass using the first
// operation of checking invalid ')' only
// first pass in order loop, remove all invalid ')' based on if the stack is empty
// second pass loop backwards, remove all invalid ')' same way
int main(){
    Solution *solution = new Solution();
    cout<<solution->minRemoveToMakeValid("l(e)))et((co)d(e")<<endl;
    cout<<solution->minRemoveToMakeValid("a)b(c)d")<<endl;
    cout<<solution->minRemoveToMakeValid("))((")<<endl;
}