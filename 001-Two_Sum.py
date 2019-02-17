class Solution:
    def twoSum(self, nums, target):               
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i,num in enumerate(nums):
            # 'enumerate(nums)' is like [(0,2),(1,7),(2,11),(3,15)] 
            if target-num in dict:                                                                                          return [dict[target-num], i]
            else:
                dict[num] = i
            # If not in dict,add it.'dict' is empty at first.
            # If 'target-num' is in 'dict', find it and return a list of index.
