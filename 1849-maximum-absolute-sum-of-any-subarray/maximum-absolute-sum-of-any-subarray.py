class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0]
        for num in nums:
         prefix.append(prefix[-1] + num)
    
        return max(prefix) - min(prefix)
      


        