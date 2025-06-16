def safe_divide(numerator, denominator):
    """
    Safely perform division with comprehensive error handling.
    
    Args:
        numerator: The number to be divided
        denominator: The number to divide by
        
    Returns:
        A string containing either the result or an error message
    """
    try:
        num = float(numerator)
        den = float(denominator)
        
        if den == 0:
            return "Error: Cannot divide by zero."
            
        result = num / den
        return f"The result of the division is {result}"
        
    except ValueError:
        return "Error: Please enter numeric values only."
    except Exception as e:
        return f"Error: An unexpected error occurred: {str(e)}"