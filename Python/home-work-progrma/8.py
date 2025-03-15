# Q8.Write a program for reversing the given number 5436 and the output should be 6345

num = int(input("Enter of Number = "))
ans = 0

while num != 0:
    re = int(num%10)
    ans = int(re + ans * 10)
    num = int(num/10)
print("reversing n = ",ans)