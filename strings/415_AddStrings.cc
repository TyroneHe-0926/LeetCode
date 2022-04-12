#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string addStrings(string num1, string num2) {
        int n1 = num1.length(), n2 = num2.length();
        if(n1 > n2){
            return this->addStrings(num2, num1);
        }

        while(n1 != n2){
            num1.insert(0,1,'0');
            n1 = num1.length();
        }
        
        vector<char> output;
        int overflow = 0;
        for(int i = n1-1; i>-1; i--){
            int digit1 = (int) num1[i] - '0', digit2 = (int) num2[i] - '0';
            int result = digit1 + digit2 + overflow;
            output.push_back((result%10)+'0');
            overflow = result >= 10;
        }
        if(overflow){
            output.push_back('1');
        }
        
        reverse(output.begin(), output.end());
        string s(output.begin(), output.end());
        return s;
    }
};

int main(){
    Solution *solution = new Solution();
    cout<<solution->addStrings("111", "123")<<endl;
    cout<<solution->addStrings("456", "77")<<endl;
    cout<<solution->addStrings("999", "999")<<endl;
    cout<<solution->addStrings("0", "0")<<endl;
}
