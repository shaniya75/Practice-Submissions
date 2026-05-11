import math
from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        D=defaultdict(list)
        dup=[]
        res=[]
        for i in range(len(nums)):
            #a=nums.index(i)
            for j in range(i+1, len(nums)):
                dup.append(nums[j])
            for k in range(i-1,-1,-1):
                dup.append(nums[k])
            D[i]=math.prod(dup)
            dup=[]

        for i in D:
            res.append(D[i])
        return res
        
            
     

        