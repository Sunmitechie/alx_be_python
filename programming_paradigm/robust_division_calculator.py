def safe_divide(numerator, denominator):
    # Check for division by zero
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        # Perform the division
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
   
