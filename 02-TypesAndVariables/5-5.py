# A program that calculates the discounted price and the reduction.

price = float(input("Enter price: "))
discount_percentage = float(input("Enter discount %: "))

reduction = price * (discount_percentage / 100)

discounted_price = price - reduction

print(f"Price with discount: {discounted_price:.2f}")
print(f"Reduction: {reduction:.2f}")