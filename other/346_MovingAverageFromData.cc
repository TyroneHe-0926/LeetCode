#include <deque>
#include <numeric>
#include <iomanip>

using namespace std;

class MovingAverage {
    deque<int> window;
    int size = 0;
    public:
        MovingAverage(int size) {
            this->size = size;
        }
        
        double next(int val) {
            if(this->window.size() < this->size){
                this->window.push_back(val);
            }
            else{
                this->window.pop_front();
                this->window.push_back(val);
            }
            return (double)accumulate(this->window.begin(), this->window.end(), 0)/(double)this->window.size();
        }
};