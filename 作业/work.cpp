#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        // 外层循环遍历每个元素
        for (int i = 0; i < n; ++i) {
            // 内层循环从 i+1 开始，避免重复使用同一个元素
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] + nums[j] == target) {
                    return { i, j }; // 返回符合条件的下标
                }
            }
        }
        return {}; // 题目保证有唯一解，此处仅为语法完整性
    }
};