def exponent_calculator(base, power):
    # Initialize result to 1
    result = 1
    
    # Calculate the result using a for loop
    for _ in range(power):
        result *= base
    
    # Display the result
    print(f"The result of {base} raised to the power of {power} is: {result}")
    
    return result

# Usage example
if __name__ == "__main__":
    base_input = int(input("Enter the base: "))
    power_input = int(input("Enter the power: "))  # Accepting power as an integer

    # Call the exponent_calculator function
    result_value = exponent_calculator(base_input, power_input)



    # To run this .py file on terminal without the terminal closing instantly
    import time
    time.sleep(120)
    input("Press Enter to exit...")
