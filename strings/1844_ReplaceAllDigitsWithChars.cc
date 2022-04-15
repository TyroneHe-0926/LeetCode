#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string replaceDigits(string s) {
        for(int i = 0; i < s.size(); i+=2){
            int shift = (int)s[i+1] - '0';
            s[i+1] = s[i] + shift;
        }
        return s;
    }
};