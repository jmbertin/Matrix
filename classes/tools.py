def custom_sum(elements):
    """
    Return the sum of a list of numbers.
    Parameters: elements (iterable): An iterable of numbers to sum.
    Returns:    float: The sum of the numbers in 'elements'.
    """
    total = 0
    for element in elements:
        total += element
    return total

def custom_abs(number):
    """
    Return the absolute value of a number.
    Parameters: number (float): The number to take the absolute value of.
    Returns:    float: The absolute value of 'number'.
    """
    if number < 0:
        return -number
    return number

def custom_sqrt(number):
    """
    Return the square root of a number.
    Parameters: number (float): The number to take the square root of.
    Returns:    float: The square root of 'number'.
    Raises:     ValueError: If 'number' is negative.
    """
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number")
    if number == 0:
        return 0

    precision = 0.00001
    estimate = number / 2 if number > 1 else 1
    while True:
        next_estimate = (estimate + number / estimate) / 2
        if custom_abs(next_estimate - estimate) < precision:
            return next_estimate
        estimate = next_estimate

def custom_round(number, decimals=0):
    """
    Round a number to a given precision in decimal digits.
    Parameters: number (float): The number to round.
                decimals (int): The number of decimal places to round to.
    Returns:    float: The rounded number.
    """
    multiplier = 10 ** decimals
    result = int(number * multiplier + (0.5 if number >= 0 else -0.5)) / multiplier
    return result

def custom_max(elements, key=lambda x: x):
    """
    Return the maximum element in an iterable based on a provided key function.
    Parameters: elements (iterable): An iterable to find the maximum element in.
                key (function): A function that takes an element and returns a value to compare.
    Returns:    object: The maximum element in 'elements' based on the 'key' function.
    """
    max_element = None
    max_key = None
    for element in elements:
        element_key = key(element)
        if max_element is None or element_key > max_key:
            max_element = element
            max_key = element_key
    return max_element
