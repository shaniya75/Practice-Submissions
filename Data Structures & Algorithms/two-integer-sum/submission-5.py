class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L=[]
        t=target
        for i in range(len(nums)):
            a=nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==t-a:
                    t=target
                    if i not in L:
                        L.append(i) 
                    if j not in L:
                        L.append(j)
                    break
        return sorted(L)