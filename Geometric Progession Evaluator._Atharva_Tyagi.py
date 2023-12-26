from Exponent_cal import exponent_calculator

def geometric_progression_sum(a, r, max_terms):
    total_sum = 0
    last_term = a  # Initialize last term with the first term

    for _ in range(max_terms):
        total_sum += a
        last_term = a  # Update last term at each iteration
        a *= r

    return total_sum, last_term, max_terms

# Get input from the user
first_term = int(input("Enter the first term: "))
common_ratio = int(input("Enter the common ratio: "))
max_terms = int(input("Enter the number of terms to calculate: "))

# Calculate and display results
sum_result, last_term_result, num_terms_result = geometric_progression_sum(
    first_term, common_ratio, max_terms
)

print(f"First term: {first_term}")
print()
print()
print()
print()
print()
print(f"Last term of the geometric progression: {last_term_result}")
print()
print()
print()
print()
print()

print(f"Common ratio: {common_ratio}")
print()
print()
print()
print()
print()
print()

print(f"Number of terms: {num_terms_result}")
print()
print()
print()
print()
print()
print()
print()

print(f"Sum of the geometric progression: {sum_result}")
print()
print()
print()
print()
print()
print()
print()


# Use the exponent_calculator function from Exponent_cal.py
exponent_calculator_result = exponent_calculator(last_term_result, num_terms_result)
print(f"The value of the last term raised to the power of the number of terms is: {exponent_calculator_result}")
