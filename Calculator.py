# Define functions for basic math operations

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

# Function to clear output (only for CMD)
def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    # Sentinel variable to control the loop
    running = True
    
    while running:
        # Display available options
        print("Welcome to the calculator!")
        print("Select operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Clear output")
        print("6. Exit")
        
        # Get user choice
        choice = input("Enter choice (1/2/3/4/5/6): ")
        
        if choice in ['1', '2', '3', '4']:
            # Get numbers from user
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            # Perform the appropriate operation
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        
        elif choice == '5':
            # Clear the screen/output
            clear()
        
        elif choice == '6':
            # Exit the loop
            running = False
            print("Exiting the calculator. Goodbye!")
        
        else:
            # Invalid choice
            print("Invalid choice! Please select a valid option.")

# Run the calculator function
if __name__ == "__main__":
    calculator()