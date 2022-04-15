#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
/*
if we see a /, indicating a possible new dir (edge case like /... and /xxx/..)
    1. check if the current tracking dir is empty, if it is, meaning we saw a grabage '/' ignore it
    2. if the current tracking dir is '.', just pass
    3. if the current tracking dir is '..', we want to pop the stack until the back of the stack is a dir (as we are going up one dir), in case if there are two '..' connected like the following one
    "/home/usr/Alpaca/./../../xxx", consider this, if we dont do that, on the second .. the stack we ended up
    being / home / usr / , since we only poped once and removed Alpaca, but going up two dir is suppose to be 
    /home/xxx, so on when we see the first .. , we should pop until the back of the stack is a dir, /home/usr, then pop usr
    4. if the current tracking dir is neither '.' or '..', we know its a new dir, push the new dir onto the stack

    5. now we need to see if we should push the '/' itself onto the stack, and this is where the edge ones come in
        if the char right after the '/' is alpha, we know its dir, then we need to push this new '/' for the upcoming dir
        if the upcoming dir is longer than '..' like '....', thats dir too, we need to push '/'
        if we are at the end of the path, then if there is a alpha in the last 2 char in the path, thats a dir too, need to push '/'
    
    6. always reset the current tracking dir at the end

else just keep adding the current char to the current tracking dir
*/
public:
    string simplifyPath(string path) {
        vector<string> stack;
        string curstr = "";
        for(int i = 0; i < path.size(); i++){
            if(path[i] == '/'){
                if(!curstr.empty()){
                    if(curstr == "."){}
                    else if(curstr == ".."){
                        if(!stack.empty()){
                            stack.pop_back();
                            while(!stack.empty() and stack.back() == "/") stack.pop_back();
                        }
                    }
                    else stack.push_back(curstr);
                }
                if(i+1 < path.size() && isalpha(path[i+1])){
                    stack.push_back("/");
                }
                else if(i+3 < path.size() && path[i+1] != '/' && path[i+2] != '/' && path[i+3] != '/'){
                    stack.push_back("/");
                }
                else if(i+3 == path.size() && (isalpha(path[i+1]) || isalpha(path[i+2]))){
                    stack.push_back("/");
                }
                curstr = "";
            }
            else curstr.push_back(path[i]);
        }

        //the last part of the path might be a dir as well, we want to make sure we include that here too
        if(!curstr.empty() && curstr != "." && curstr != "..") stack.push_back(curstr);
        //the last part of the path might be a .., we want to go back to the prev dir
        if(curstr == ".." && !stack.empty()){
            stack.pop_back();
            while(!stack.empty() and stack.back() == "/") stack.pop_back();
        }
        //in cases like /../ where the whole stack would be empty after processing, we need at least the root
        if(stack.empty()) stack.push_back("/");
        
        string result = "";
        for(auto s : stack) result.append(s);
        return result;
    }
};

int main(){
    Solution *solution = new Solution();
    cout<<solution->simplifyPath("/home/")<<endl;
    cout<<solution->simplifyPath("/../")<<endl;
    cout<<solution->simplifyPath("/home")<<endl;
    cout<<solution->simplifyPath("/home//foo/")<<endl;
    cout<<solution->simplifyPath("/a/../../b/../c//.//")<<endl; // "/c"
    cout<<solution->simplifyPath("////home/usr/Alpaca/./../../xxx")<<endl; // "/home/xxx"
    cout<<solution->simplifyPath("/a//b////c/d//././/..")<<endl; // "/a/b/c"
}