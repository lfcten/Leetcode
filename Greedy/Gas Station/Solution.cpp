class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int res = 0, total = 0, s = 0;

        for (int i = 0; i < gas.size(); i++){
            res += gas[i] - cost[i];
            if (res < 0){
                s = i + 1;
                total += res;
                res = 0;
            }
        }

        if (res + total >= 0){
            return s;
        } else{
            return -1;
        }
    }
};