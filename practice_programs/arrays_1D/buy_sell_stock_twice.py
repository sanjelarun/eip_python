def buy_sell_stock_twice(prices):
    maximum_profit, min_price_so_far = 0, float('inf')
    sum_max  = len(prices) * [0]
    for i,price in enumerate(prices):
        maximum_profit_today = price - min_price_so_far
        maximum_profit = max(maximum_profit, maximum_profit_today)
        min_price_so_far = min(min_price_so_far, price)
        sum_max[i] = maximum_profit
    max_price_so_far = float('-inf')
    for i,price in reversed(list(enumerate(prices[1:],1))):
        max_price_so_far = max(max_price_so_far,price )
        maximum_profit = max(maximum_profit, max_price_so_far - price + sum_max[i-1])
    return maximum_profit

print(buy_sell_stock_twice([100,8,3,2,1]))