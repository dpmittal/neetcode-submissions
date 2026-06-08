class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s:
            if(hashmap.get(i)==None):
                hashmap[i] = 1
            else:
                hashmap[i]+=1
        
        for i in t:
            if(hashmap.get(i)==None or hashmap.get(i)<=0):
                return False
            else:
                hashmap[i]-=1
        
        for key, item in hashmap.items():
            if(item!=0):
                return False
        return True