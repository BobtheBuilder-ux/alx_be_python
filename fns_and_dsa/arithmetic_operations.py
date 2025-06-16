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
        return float(num1 + num2)
    elif operation == "subtract":
        return float(num1 - num2)
    elif operation == "multiply":
        return float(num1 * num2)
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return float(num1 / num2)
    else:
        return f"Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'"