Class Solution{
public:
    int jump(vector<int>& nums){
        int local = 0, global = 0, step = 0;
        for (int i = 0; i < nums.size(); i++){
            if (i > local){
                local = global;
                step++;
            }
            global = max(global, i + nums[i]);
            # todo: 到达终点即停止
        }
        return step;
    }
}