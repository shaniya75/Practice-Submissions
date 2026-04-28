class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        S=sorted(list(s))
        L=sorted(list(t))
        if S==L:
            return True
        else:
            return False

