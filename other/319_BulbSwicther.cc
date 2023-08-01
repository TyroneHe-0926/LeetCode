#include <iostream>
using namespace std;

class Solution {
public:
    int bulbSwitch(int n) {
        bool* bulbs = new bool[n]();
        for(int i = 0; i < n; ++i){
            bulbs[i] = 1;
        }

        int count = 2;
        while(count <= n){
            for(int i = 0; i < n; ++i){
                if((i+1) % count == 0){
                    bulbs[i] = !bulbs[i];
                }
            }
            ++count;
        }

        int res = 0;
        for(int i = 0; i < n; ++i){
            if (bulbs[i])
            {
                ++res;
            }
            
        }
        delete[] bulbs;

        // cout<<res<<endl;
        return res;
    }
};

int main(){
    Solution s {};
    s.bulbSwitch(2353535);
}