# Q9.Write a program to check if a given number 371 is an Armstrong number? 

num = int(input("Enter of Number = "))
ans = 0
t = num
while num != 0:
    re = int(num%10)
    ans = int(re * re * re)
    num = int(num/10)

if(t == ans):
    print("Is Armstrong Number ")
else:
    print("Is not Armstrong Number ")
