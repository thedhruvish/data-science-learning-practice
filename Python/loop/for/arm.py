def is_armstrong_number(num):
  """
  This function checks if a number is an Armstrong number.

  Args:
      num: The integer to be checked.

  Returns:
      True if the number is an Armstrong number, False otherwise.
  """

  original_num = num
  sum = 0
  number_of_digits = len(str(num))

  # Iterate through each digit of the number
  for digit in str(num):
    # Raise the digit to the power of the number of digits and add to the sum
    sum += int(digit) ** number_of_digits

  # Check if the sum is equal to the original number
  return sum == original_num

# Get input from the user
number = int(input("Enter a number: "))

# Check if the number is Armstrong
if is_armstrong_number(number):
  print(f"{number} is an Armstrong number")
else:
  print(f"{number} is not an Armstrong number")
