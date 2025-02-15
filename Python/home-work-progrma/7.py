# Q7.Write a program for sum of digits.the digits are 76543 and the output should be 25. 

num = int(input("Enter of Number = "))
ans = 0
while num != 0:
    re = int(num%10)
    ans = ans + re
    num = int(num/10)

print("Ans = " , ans)