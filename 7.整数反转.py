#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (32.43%)
# Likes:    1196
# Dislikes: 0
# Total Accepted:    156.5K
# Total Submissions: 478.1K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        int_str = str(x)
        int_str_list = list(int_str)
        int_str_new_list = list()
        # 先判断正整数
        if x >= 0:
            for param in range(len(int_str_list)):
                int_str_new_list.append(int_str_list.pop(-1))
            if int_str_new_list[0] == "0" and len(int_str_new_list) != 1:
                int_str_new_list.pop(0)
            res = int("".join(int_str_new_list))
        else:
            int_str_new_list.append(int_str_list.pop(0))
            for param in range(len(int_str_list)):
                int_str_new_list.append(int_str_list.pop(-1))
            if int_str_new_list[1] == "0":
                int_str_new_list.pop(1)
            res = int("".join(int_str_new_list))
        if abs(res) >= abs(pow(2, 31)):
            return 0
        else:
            return res
