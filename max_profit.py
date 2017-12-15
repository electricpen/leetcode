def max_profit(prices):
    best_price = 0
    if prices is None:
        return 0

    def permutations(prices, current_price=0, profit=0, buy=True):
        nonlocal best_price
        if len(prices) == 1:
            if not buy:
                if prices[0] < current_price:
                    profit += prices[0] - current_price
            if profit > best_price:
                best_price = profit
        else:
            for price in prices:
                if buy:
                    permutations(prices[1:], price, profit, False)
                else:
                    if price > current_price:
                        permutations(prices[1:], 0, profit +
                                     (price - current_price), True)

    permutations(prices)

    return best_price


print(max_profit([20, 80, 50, 100, 20]))
