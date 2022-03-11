class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            cmpt = target - nums[i] # complement
            if cmpt in hashmap and hashmap[cmpt] != i:
                return [i, hashmap[cmpt]]
        