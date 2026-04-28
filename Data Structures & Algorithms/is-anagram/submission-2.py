class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        L=list(s)
        L2=list(t)
        if sorted(L)==sorted(L2):
            return True
        else:
            return False
        