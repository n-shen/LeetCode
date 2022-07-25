class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = m - 1, n - 1
        ptr3 = m + n - 1

        while ptr2 >= 0:
            if ptr1 < 0 or nums2[ptr2] > nums1[ptr1]:
                nums1[ptr3] = nums2[ptr2]
                ptr2 -= 1
            else:
                nums1[ptr3] = nums1[ptr1]
                ptr1 -= 1
            ptr3 -= 1
            