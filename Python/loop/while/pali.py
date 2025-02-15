num = int(input("Enter of Number : "))

sum = 0
t = num;
while num != 0:
    rem = int(num % 10)
    sum = sum * 10 + rem
    num = int(num / 10 )


if t == sum:
    print(t," Is Palindrom Number")
else:
   print(t," Not Palindrom Number")
