class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(n):
            a=nums[i]
            for j in range(i+1,n):
                if nums[j]==a:
                    return True
        return False
        