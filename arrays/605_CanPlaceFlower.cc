#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int count = 0, len = flowerbed.size();
        if(n == 0) return true;
        for(int i = 0; i < len; i++){
            if(i != 0 && i != len-1 && flowerbed[i-1] == 0 && flowerbed[i+1] == 0 && flowerbed[i] == 0){
                count++;
                flowerbed[i] = 1;
            }
            if(i == 0 && flowerbed[i] == 0){
                if(i + 1 < len && flowerbed[i+1] == 0){
                    count++;
                    flowerbed[i] = 1;
                }
                else if(i+1>len-1){
                    count++;
                    flowerbed[i] = 1;
                }
            }
            if(i == len-1 && flowerbed[i] == 0){
                if(i - 1 > -1 && flowerbed[i-1] == 0){
                    count++;
                    flowerbed[i] = 1;
                }
                else if(i - 1 < 0){
                    count++;
                    flowerbed[i] = 1;
                }
            }
            if(count == n) return true;
        }
        return false;
    }
};