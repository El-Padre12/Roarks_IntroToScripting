# Angel Chavez
# Aug 30th, 2025
# Python 3.13.5
# calculator program that demonstrates the use of exception handling in python

def get_number(prompt):
    """
    Get a valid number from user input with error handling.
    
    Args:
        prompt (str): The prompt message to display to user
        
    Returns:
        float: Valid numeric value entered by user
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number (e.g., 5, 3.14, -2)")

def get_operator():
    """
    Get a valid operator from user input with validation.
    
    Returns:
        str: Valid operator (+, -, *, /)
    """
    valid_operators = ['+', '-', '*', '/']
    
    while True:
        operator = input("Enter an operator (+, -, *, /): ").strip()
        
        # Validate operator using conditional logic
        if operator in valid_operators:
            return operator
        else:
            print(f"Error: '{operator}' is not a valid operator. Please use +, -, *, or /")

def perform_calculation(num1, operator, num2):
    """
    Perform the calculation based on the operator.
    
    Args:
        num1 (float): First number
        operator (str): Mathematical operator
        num2 (float): Second number
        
    Returns:
        float: Result of the calculation
        
    Raises:
        ZeroDivisionError: When attempting to divide by zero
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check for division by zero before performing operation
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2

def main():
    """
    Main calculator function that runs the interactive loop.
    """
    print("Welcome to the Tutoring Center Calculator!")
    
    # Main program loop - continues until user chooses to exit
    while True:
        try:
            print("-" * 40)
            
            # Get first number with exit option
            first_input = input("Enter the first number (or 'quit'/'exit' to stop): ").strip().lower()
            if first_input in ['quit', 'exit']:
                print("Thank you for using the calculator! Keep practicing!")
                break
            
            # Convert first input to number
            try:
                num1 = float(first_input)
            except ValueError:
                print("Error: Please enter a valid number (e.g., 5, 3.14, -2)")
                continue
            
            # Get operator
            operator = get_operator()
            
            # Get second number
            num2 = get_number("Enter the second number: ")
            
            # Perform calculation with division by zero protection
            try:
                result = perform_calculation(num1, operator, num2)
                
                # Display the result with proper formatting
                if result == int(result):
                    # Display as integer if result is a whole number
                    print(f"Result: {num1} {operator} {num2} = {int(result)}")
                else:
                    # Display as float with precision
                    print(f"Result: {num1} {operator} {num2} = {result:.6g}")
                    
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed! Please try again with a non-zero divisor.")
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n Calculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()