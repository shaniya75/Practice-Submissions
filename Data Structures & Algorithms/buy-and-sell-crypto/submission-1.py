class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        if sorted(prices, reverse=True)==prices:
            return 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                buy=min(prices[i],prices[j])
                if prices[j]-buy>0:
                    res=max(res,prices[j]-buy)
        return res

        