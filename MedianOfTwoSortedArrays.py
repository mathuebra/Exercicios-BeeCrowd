from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = sorted(nums1+nums2)
        if len(new_list) % 2 == 1:
            return float(new_list[math.floor(len(new_list)/2)])
        else:
            return float((new_list[math.floor(len(new_list)/2)] + new_list[math.floor(len(new_list)/2)-1])/2)
        
print(Solution().findMedianSortedArrays(nums1=[0, 0], nums2=[0, 0]))