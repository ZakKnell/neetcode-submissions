#include <vector>

class MinStack {
public:
    MinStack() {
        
    }
    
    void push(int val) {
        if (minValues.empty()) {
            minValues.push_back(val);
        }
        else if (val <= minValues.back()) {
            minValues.push_back(val);
        }
        allValues.push_back(val);
    }
    
    void pop() {
        if (allValues.back() == minValues.back()) {
            minValues.pop_back();
        }
        allValues.pop_back();
    }
    
    int top() {
        return allValues.back();
    }
    
    int getMin() {
        return minValues.back();
    }
private:
    std::vector<int> minValues;
    std::vector<int> allValues;

};
