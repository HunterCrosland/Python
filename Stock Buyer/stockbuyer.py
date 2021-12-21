def maxProfit(prices: list) -> int:

    min = prices[0]
    profit = 0

    for num in prices:
        if min > num:
            min = num
        if num - min > profit:
            profit = num - min

    return profit 
