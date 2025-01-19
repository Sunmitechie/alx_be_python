def safe_divide(numerator, denominator):
    """
    Perform division, handling division by zero and non-numeric input errors.

    Args:
        numerator: The number to be divided (expected as a string or numeric).
        denominator: The number to divide by (expected as a string or numeric).

    Returns:
        str: Result of the division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        numumerator = float(numerator)
        denominator = float(denominator)

        # Check for division by zero
    if denominator == 0:
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

        # Perform the division
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"

    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
