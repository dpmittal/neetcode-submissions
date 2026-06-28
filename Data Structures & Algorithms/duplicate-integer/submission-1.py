class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = [0]*(100001)
        for i in nums:
            if store[i]!=0:
                return True
            store[i] = 1
        return False
