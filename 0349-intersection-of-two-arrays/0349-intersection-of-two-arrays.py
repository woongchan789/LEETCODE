class Solution(object):
    def intersection(self, nums1, nums2):
        a = len(nums1)
        b = len(nums2)
        
        final = []
        
        if a < b:
            for i in nums1:
                if (i in nums2) and (i not in final):
                    final.append(i)
        else:
            for i in nums2:
                if (i in nums1) and (i not in final):
                    final.append(i)
                    
        return final
        