# Angel Chavez
# Sept 2, 2025
# Python 3.13.5
# A robust calculator that handles user input errors gracefully
# and uses assertions to verify operator validity during development.
# Supports basic arithmetic operations: +, -, *, /

def get_number(prompt):
    """Get a valid number from user input with error handling."""

    while True:
        try:
            # Attempt to convert user input to float
            value = float(input(prompt))
            return value
        except ValueError:
            # Handle non-numeric input
            print("Error: Please enter a valid number.")

def get_operator():
    """Get a valid operator from user input."""

    valid_operators = ['+', '-', '*', '/']
    
    while True:
        operator = input("Enter an operator (+, -, *, /): ").strip()
        
        # Use assertion to verify operator is valid during development
        # This helps catch programming errors if invalid operators slip through
        try:
            assert operator in valid_operators, f"Invalid operator: {operator}"
            return operator
        except AssertionError as e:
            print(f"Error: {e}")
            print("Please enter one of the following: +, -, *, /")

def calculate(num1, num2, operator):
    """Perform the calculation based on the operator."""

    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # This will raise ZeroDivisionError if num2 is 0
            result = num1 / num2
        
        return result
    
    except ZeroDivisionError:
        # Handle division by zero specifically
        print("Error: Cannot divide by zero!")
        return None

def main():
    """Main calculator loop."""
    
    print("Welcome to the Exception-Safe Calculator!")
    print("This calculator supports +, -, *, / operations")
    print("-" * 40)
    
    while True:
        try:
            # Get first number with error handling
            num1 = get_number("Enter the first number: ")
            
            # Get second number with error handling  
            num2 = get_number("Enter the second number: ")
            
            # Get operator with assertion validation
            operator = get_operator()
            
            # Perform calculation with division by zero handling
            result = calculate(num1, num2, operator)
            
            # Display result if calculation was successful
            if result is not None:
                print(f"\nResult: {num1} {operator} {num2} = {result}")
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nCalculator interrupted by user.")
            break
        except Exception as e:
            # Catch any unexpected errors
            print(f"An unexpected error occurred: {e}")
        
        # Ask if user wants to continue
        print("\n" + "-" * 40)
        continue_choice = input("Would you like to perform another calculation? (y/n): ").lower().strip()
        
        if continue_choice not in ['y', 'yes']:
            break
    
    print("Thank you for using the Exception-Safe Calculator!")

# Run the calculator if this script is executed directly
if __name__ == "__main__":
    main()