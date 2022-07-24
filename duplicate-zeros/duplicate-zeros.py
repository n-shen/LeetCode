class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        lg = len(arr)
        ptr1, ptr2 = 0, lg - 1
        endZero = False
        
        while ptr1 <= ptr2:
            if arr[ptr1] == 0:
                if ptr2 == ptr1:
                    endZero = True
                    break
                arr[ptr2] = 0
                ptr2 -= 1
            ptr1 += 1
        
        # print(ptr1, ptr2, arr)
        
        if endZero:
            ptr2 = lg - 2
        else:
            ptr2 = lg - 1
        ptr1 -= 1 
        # print(ptr1, ptr2, arr)
             
        while ptr1 != ptr2:
            if arr[ptr1] != 0:
                arr[ptr2] = arr[ptr1]
                arr[ptr1] = 0
            else:
                ptr2 -= 1
            ptr1 -= 1
            ptr2 -= 1
        # print(ptr1, ptr2, arr)
                
        