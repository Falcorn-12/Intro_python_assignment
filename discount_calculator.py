def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    price_input = float(input("Enter the original price of the item: "))
    discount_input = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(price_input, discount_input)

    # Print the result
    if discount_input >= 20:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")