n1 = int(input("Enter of Start Number : "))
n2 = int(input("Enter of End Number : "))
div = int(input("Enter of divi Number :"))

while n1 < n2:
    if n1 % div == 0:
        print(n1)
    n1 = n1 + 1
