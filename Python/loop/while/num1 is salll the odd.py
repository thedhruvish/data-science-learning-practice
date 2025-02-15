num1 = int(input("Enter of Number : "))
num2 = int(input("Enter of Number : "))

if num1 < num2:
    while num1 <= num2:
        if num1 % 2 == 1:
            print(num1)
        num1 = num1 + 1

else:
    while num1 >= num2:
        if num2 % 2 == 0:
            print(num2)
        num2 = num2 + 1
