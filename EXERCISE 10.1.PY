prices=list(map(float ,input("Enter asset costs separated by spaces:").split()))

prices.sort(reverse=True)

print("prices from highest to lowest:")

print(prices)

print("top three priciest entries:")

for price in prices[:3]:
    print(price)
    
    
    
    
    
    
    
    
    