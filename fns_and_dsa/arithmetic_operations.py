# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        num1: First number
        num2: Second number
        operation: Operation to perform ('add', 'subtract', 'multiply', 'divide')
        
    Returns:
        Result of operation or error message for division by zero
    """
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        result = num1 / num2
    else:
        return "Error: Invalid operation"
    
    return float(result)