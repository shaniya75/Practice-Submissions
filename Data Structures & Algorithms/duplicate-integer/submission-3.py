class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        L=[]
        for i in range(len(nums)):
            a=nums[i]
            for j in range (i+1,len(nums)):
                if a==nums[j]:
                    return True
                    break
        return False      