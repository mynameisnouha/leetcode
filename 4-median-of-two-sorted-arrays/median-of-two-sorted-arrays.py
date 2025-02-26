class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        sorted_arr=sorted(nums1+nums2)
        n=len(sorted_arr)
        if n % 2 == 1:
            return sorted_arr[n // 2]
        else:
            
            return ((float(sorted_arr[n // 2 - 1]) + float(sorted_arr[n // 2])) / 2)
        