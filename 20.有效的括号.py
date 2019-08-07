#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (38.16%)
# Likes:    954
# Dislikes: 0
# Total Accepted:    102.2K
# Total Submissions: 261.5K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#
class Solution:
    def isValid(self, s: str) -> bool:
        # stack method            
        push_dict = {
            "[": 1, 
            "{": 2,
            "(": 3
        }
        pop_dict = {
            "]": 1, 
            "}": 2, 
            ")": 3
        }
        if s == "":
            return True
        if s[0] in pop_dict:
            return False
        this_list = []
        for str in s:
            if this_list == []:
                this_list.append(str)
            else:
                if str in push_dict:
                    this_list.append(str)
                else:
                    if pop_dict[str] == push_dict[this_list[-1]]:
                        this_list.pop()
                    else:
                        return False
        if this_list == []:
            return True
        return False

