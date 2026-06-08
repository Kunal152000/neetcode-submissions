class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         profit = max(profit,prices[j]-prices[i])
        
        # return profit
        profit = 0
        buy_day = 0
        sell_day = 1
        while sell_day<len(prices):
            if prices[buy_day]< prices[sell_day]:
                profit = max(profit,prices[sell_day]-prices[buy_day])
            else:
                buy_day = sell_day

            sell_day +=1

        return profit
                
        