def divisible_by_ten(num):
    """
    Check if a number is divisible by ten.
    
    :param num: int or float
    :return: bool
    """
    # Validate input
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be an integer or float.")

    if num % 10 == 0:
        return True
    else:
        return False

print(divisible_by_ten(20))  # True
print(divisible_by_ten(25))  # False