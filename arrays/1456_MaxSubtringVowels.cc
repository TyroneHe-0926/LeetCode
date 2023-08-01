#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {
    unordered_set<char> vowels = {'a','e','i','o','u'};
public:
    int maxVowels(string s, int k) {
        int left = 0, right = k-1;
        int maxlen = 0;
        while(right < s.length()){
            string curVowel = s.substr(left, k);
            maxlen=max(checkVowels(curVowel), maxlen);
            ++left;
            ++right;
        }
        return maxlen;
    }

    int checkVowels(string s){
        int count = 0;
        for(auto c : s){
            if(vowels.find(c) != vowels.end()){
                ++count;
            }
        }
        return count;
    }
};

// class Solution:
//     def maxVowels(self, s: str, k: int) -> int:
//         left, right = 0, k-1
//         maxlen = 0
//         while right < len(s):
//             cur_vowel = self.checkVowels(s[left:right+1])
//             maxlen = max(cur_vowel, maxlen)
//             left+=1
//             right+=1
        
//         return maxlen

//     def checkVowels(self, s: str) -> int:
//         count = 0
//         for c in s:
//             if c in ['a','e','i','o','u']:
//                 count+=1
//         return count


int main(){
    Solution s{};
    s.maxVowels("abciiidef",3);
    s.maxVowels("aeiou",2);
    s.maxVowels("leetcode",3);
}