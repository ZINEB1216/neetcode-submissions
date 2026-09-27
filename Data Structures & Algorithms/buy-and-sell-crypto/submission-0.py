class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        for i in range(len(prices)):
            for j in range(len(prices)):
                if i <= j and prices[j] - prices[i] >= 0:
                    diff.append(prices[j] - prices[i])
        return max(diff)