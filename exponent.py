def large_power(base, exponent):
    """
    Calculate base raised to exponent and check if result > 5000.
    
    :param base: int or float
    :param exponent: int
    :return: (result, is_large) tuple
    """
    # Validate inputs
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float.")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer.")
    if base == 0 and exponent <= 0:
        raise ValueError("0 raised to a non-positive exponent is undefined.")
    
    # Calculate and check
    result = base ** exponent
    is_large = result > 5000
    return result, is_large


print("Welcome to the Large Power Calculator!")
try:
    base = float(input("Enter the base number: "))
    exponent = int(input("Enter the exponent: "))
    
    result, is_large = large_power(base, exponent)
    
    if is_large:
        print(f"{base} ^ {exponent} = {result} → LARGE")
    else:
        print(f"{base} ^ {exponent} = {result} → NOT LARGE")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
