class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L=[]
        
        for i in range(len(nums)):
            a=nums[i]
            for j in range(i+1, len(nums)):
                if ((target-a)==nums[j]):
                    L.append(i)
                    L.append(j)
                    

                
        return L    