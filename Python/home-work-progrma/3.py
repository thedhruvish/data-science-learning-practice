# Q3.Write a program that prints all prime numbers between 0 to 50. 

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(51):
    if is_prime(i):
        print(i)
