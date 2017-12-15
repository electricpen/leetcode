def max_profit(prices):
    if prices is None:
        return 0

    def permutations(prices, current_price=0, profit=0, buy=True, results=[]):
        if len(prices) == 1:
            if not buy:
                if prices[0] > current_price:
                    profit += prices[0] - current_price
            results.append(profit)
        else:
            for index, price in enumerate(prices):
                if buy:
                    permutations(prices[index + 1:], price, profit, False)
                else:
                    if price > current_price:
                        permutations(prices[index + 1:], 0, profit +
                                     (price - current_price), True)
        return results

    results = permutations(prices)
    for price in results:
        if price > best_price:
            best_price = price
    return best_price


print(max_profit([10, 20, 1000, 0]))
