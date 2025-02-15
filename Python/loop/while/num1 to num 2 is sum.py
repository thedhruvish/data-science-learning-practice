num1 = int(input("Enter of Number : "))
num2 = int(input("ENter of Number : "))

ans = 0
while num1 < num2:
    ans = num1 + ans
    num1 = num1 + 1

print("\nTotal Number of ",ans)
