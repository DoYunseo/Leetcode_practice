from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ptr1, ptr2 = 0, 0 
        merge = []

        #merge sorted arrays

        while ptr1 < len(nums1) or ptr2 < len(nums2):
            if ptr1 < len(nums1) and (ptr2 >= len(nums2) or nums1[ptr1] <= nums2[ptr2]):
                merge.append(nums1[ptr1])
                ptr1 += 1
            elif ptr2 < len(nums2):
                merge.append(nums2[ptr2])
                ptr2 += 1
        while ptr1 < len(nums1):
            merge.append(nums1[ptr1])
            ptr1 += 1
        while ptr2 < len(nums2):
            merge.append(nums2[ptr2])
            ptr2 += 1
            
        n = len(merge)
        if n % 2 == 1:
            return merge[n//2]
        else:
            return (merge[n//2] + merge[n//2 - 1])  / 2
        
                    