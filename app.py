def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

print("Total Bill:", calculate_total([10, 20, 30]))

def calculate_total(prices, discount=0, tax_rate=0.05):
    total = sum(prices) - discount
    return total + (total * tax_rate)

print("Total Bill:", calculate_total([10, 20, 30], 5))

echo 'print("Calculating final total...")' >> app.py
