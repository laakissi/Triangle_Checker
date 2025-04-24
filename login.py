import re

# Sample usernames and passwords
SAMPLE_USERNAMES = ["Abcde", "kymn12"]
SAMPLE_PASSWORDS = ["mySWUST", "helloSW"]

def is_triangular(a, b, c):
    """Check if three numbers satisfy the Triangle Inequality Theorem."""
    return a + b > c and a + c > b and b + c > a

def get_number_input(prompt):
    """Prompt user for a number and restart the program if it's 0 or negative."""
    try:
        num = float(input(prompt))
        if num <= 0:
            print("Error: Invalid input. The number must be greater than zero.")
            print("The program will restart...\n")
            main()  # Restart the program
            return None  
        return num
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
        print("The program will restart...\n")
        main()  # Restart the program
        return None  

def login():
    """Handle user authentication with predefined credentials."""
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if username in SAMPLE_USERNAMES and password in SAMPLE_PASSWORDS:
        print("Login successful!\n")
        return True
    else:
        print("Invalid username or password. Exiting program.")
        exit()

def main():
    """Main execution function."""
    if login():
        print("Enter three positive numbers to check if they form a triangle:")
        a = get_number_input("Enter first number: ")
        if a is None: return  
        b = get_number_input("Enter second number: ")
        if b is None: return  
        c = get_number_input("Enter third number: ")
        if c is None: return  

        if is_triangular(a, b, c):
            print("The numbers form a valid triangle.")
        else:
            print("The numbers do NOT form a triangle.")

if __name__ == "__main__":
    main()