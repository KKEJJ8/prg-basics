# Initial account balance
account_balance = 500

# List of purchase amounts
purchase_amounts = [140, 499, 500, 501, 720]

# Process each payment
for total_payment in purchase_amounts:
    if total_payment <= account_balance:
        print(f"Payment for {total_payment} completed.")
        account_balance -= total_payment  # Deduct the paid amount from the balance
    else:
        print(f"No funds for {total_payment}.")