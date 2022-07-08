class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked = {}
        for e in nums:
            if e in checked:
                return True
            checked[e] = 1
        # print(checked)
        return False
            