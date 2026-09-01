transactions = []

for i in range(5):
    amount = float(input("Enter transaction amount: "))
    transactions.append(amount)

largest = max(transactions)
average = sum(transactions) / 5

print("Transactions:", transactions)
print("Largest:", largest)
print("Average:", average)
