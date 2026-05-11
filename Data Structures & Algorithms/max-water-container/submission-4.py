class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        for i in range(len(heights)):
            left=i
            for j in range(i+1, len(heights)):
                height=min(heights[i],heights[j])
                width=j-i
                res=max(res, height*width)
        return res   