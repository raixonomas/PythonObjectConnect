# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

profit = 0
bought = 0
sold = 0

for buy in prices:
    boughtTemp = buy
    for sell in prices[prices.index(buy):]:
        soldTemp = sell
        profitTemp = soldTemp - boughtTemp
        if profitTemp > profit:
            profit = profitTemp
            bought = boughtTemp
            sold = soldTemp


print("Bought : " + str(bought))
print("Sold : " + str(sold))
print("Profit : " + str(profit))