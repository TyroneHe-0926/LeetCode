#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int height = grid.size(), width = grid[0].size();
        for(int i = 0; i < k; i++){
            grid = this->shift(grid, width, height);
        }
        return grid;
    }

    vector<vector<int>> shift(vector<vector<int>>&src, int width, int height){
        vector<vector<int>> result(height, vector<int>(width));
        for(int i = 0; i < height; i++){
            for(int j = 0; j < width; j++){
                if(i == height-1 && j == width-1){
                    result[0][0] = src[i][j];
                }
                else if(j == width - 1){
                    result[i+1][0] = src[i][j];
                }
                else{
                    result[i][j+1] = src[i][j];
                }
            }
        }
        return result;
    }
};