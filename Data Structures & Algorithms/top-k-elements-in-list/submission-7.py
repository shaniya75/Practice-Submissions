from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D={}
        L=[[] for i in range(len(nums)+1)]
        for i in nums:
            D[i]=1+D.get(i,0)
        for n,c in D.items():
            L[c].append(n)
        res=[]
        for i in range(len(L)-1,-1,-1):
            for j in L[i]:
                res.append(j)
                if len(res)==k:
                    return res
        