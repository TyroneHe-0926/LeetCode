#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int height = board.size(), width = board[0].size();
        int alive = 0;
        vector<vector<int>> tempBoard = board; 
        for(int row = 0; row < height; row++){
            for(int col = 0; col < width; col++){
                alive = this->getAliveNeighbors(row, col, tempBoard, width, height);
                if(board[row][col] == 1){
                    if(alive > 3 || alive < 2){
                        board[row][col] = 0;
                    }
                }
                else{
                    alive == 3 ? board[row][col] = 1 : board[row][col] = 0;
                }
            }
        }
    }

    int getAliveNeighbors(int row, int col, vector<vector<int>> board, int width, int height){
        int count = 0;
        row - 1 > -1 && board[row-1][col] == 1 ? count++ : 0; //down
        row + 1 < height && board[row+1][col] == 1 ? count++ : 0; //up
        col - 1 > -1 && board[row][col-1] == 1 ? count++ : 0; //left
        col + 1 < width && board[row][col+1] == 1 ? count++ : 0; //right
        row - 1 > -1 && col - 1 > -1 && board[row-1][col-1] == 1 ? count++ : 0; //up left
        row - 1 > -1 && col + 1 < width && board[row-1][col+1] == 1 ? count++ : 0; //up right
        row + 1 < height && col - 1 > -1 && board[row+1][col-1] == 1 ? count++ : 0; //down left
        row + 1 < height && col + 1 < width && board[row+1][col+1] == 1 ? count++ : 0; //down right
        return count;
    }
};