class Solution:
    def intersection( self,nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set([num for num in nums1 if num in nums2]))