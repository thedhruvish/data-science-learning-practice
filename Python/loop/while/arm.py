num = int(input("Enter of Number :"))

sum = 0
temp = num
while num > 0:
    rem = int(num % 10)
    sum = sum + rem * rem * rem
    num = int(num/10)
    


if temp == sum:
    print(temp," Is Armstrong Number")
else:
    print(temp," Not Armstrong Number")
