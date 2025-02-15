# Define the input as a string
input_string = '1*23-1/3'

# Initialize variables
num = ''
exp = ''
ans = 0
current_number = ''

# Iterate through each character in the input string
for char in input_string:
    if char.isdigit():
        current_number += char  # Build the current number string
    else:
        if current_number:  # If we have a current number, append it to num
            num += current_number + ' '  # Add a space for separation
            current_number = ''  # Reset current number
        exp += char + ' '  # Add operator to exp

# Append the last number if there's any
if current_number:
    num += current_number

# Remove any trailing spaces
num = num.strip()
exp = exp.strip()

# Split the num and exp strings into their respective parts
num_parts = num.split()
exp_parts = exp.split()

# Check if the number of operators is valid
if (len(num_parts) - 1) == len(exp_parts):
    ans = int(num_parts[0])  # Start with the first number

    # Perform the operations based on the operators
    for i in range(len(exp_parts)):
        if exp_parts[i] == '*':
            ans *= int(num_parts[i + 1])
        elif exp_parts[i] == '-':
            ans -= int(num_parts[i + 1])
        elif exp_parts[i] == '+':
            ans += int(num_parts[i + 1])
        elif exp_parts[i] == '/':
            ans /= int(num_parts[i + 1])

print(ans)