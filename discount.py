def calculate_discount(price, discount_percentage):
    """
    Calculate the discounted price based on the original price and discount percentage.

    :param price: Original price of the item
    :param discount_percentage: Discount percentage to apply
    :return: Discounted price
    """
    # Check if discount percentage is 20% or higher
    # If so, calculate the discount amount and return the discounted price  
     # Validate inputs
    if original_price < 0 or discount_percentage < 0:
        raise ValueError()
    elif discount_percentage >= 20:
        discount_amount = (discount_percentage / 100) * price
        discounted_price = price - discount_amount
    else:
        discounted_price = price
    return discounted_price

print("Welcome to the Discount Calculator!")
# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate final price after discount
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display the result
    if final_price < original_price:
        print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")