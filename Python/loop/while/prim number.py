n = int(input("Enter of number = "))
a=2
teap=1



while n>a:
    if n%a==0:
        teap=0
    a = a + 1

if teap==1:
    print(n," is prime Number")
else:
    print(n,"is not prime Number")

