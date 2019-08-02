#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (28.89%)
# Likes:    1025
# Dislikes: 391
# Total Accepted:    234K
# Total Submissions: 809.3K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <3:
            return 0

        digits = [0]*n
        count = 1
        sq = int(n**0.5)+1

        for i in range(3, n, 2):
            if not digits[i]:
                count += 1
                if i > sq:
                    continue
                for j in range(i+i, n, i):
                    digits[j] = 1

        return count

