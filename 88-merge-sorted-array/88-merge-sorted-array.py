class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        nums1.reverse()
        for i in range(0, len(nums1)):
            if i < len(nums2):
                nums1[i] = nums2[i]
            i += 1
        
        nums1.sort()
        