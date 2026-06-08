class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for i in nums:
            if store.get(i)!=None:
                return True
            store[i] = True
        return False
