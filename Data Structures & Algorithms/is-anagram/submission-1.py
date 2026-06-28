class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0]*26
        ascii_a = ord('a')
        for i in s:
            count[ord(i)-ascii_a]+=1
        for i in t:
            count[ord(i)-ascii_a]-=1
        
        for c in count:
            if c!=0:
                return False
        return True