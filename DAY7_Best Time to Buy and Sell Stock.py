class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        minValue=prices[0]
        result=0
        for index in range(n):
            minValue=min(minValue,prices[index])
            result=max(result,prices[index]-minValue)
        return result
        
