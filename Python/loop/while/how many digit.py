# how many digits

num = int(input("Enter of Number :"))

i = 0
while num > 0:
    rem = int(num % 10)
    num = int(num/10)
    i = i + 1    

print(i," Is Digit ")
