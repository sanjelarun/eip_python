def maximum_stock_profit(prices):
    maximum_profit, min_price_so_far = 0, float('inf')
    for price in prices:
        maximum_profit_today = price - min_price_so_far
        maximum_profit = max(maximum_profit, maximum_profit_today)
        min_price_so_far = min(min_price_so_far, price)
    return maximum_profit


print(maximum_stock_profit([20,30,21,34,12,11]))