class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        freq2={}
        if len(s)!=len(t):
            return False
        
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        
        for ch in t:
            if ch not in freq:
                return False
            freq[ch]-=1
            if freq[ch] < 0:
                return False
        return True