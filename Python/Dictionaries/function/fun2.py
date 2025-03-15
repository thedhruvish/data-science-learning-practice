def arm():
    num = int(input("Enter of Number :"))
    ans = 0
    t = num
    while num != 0:
        rem = int(num % 10)
        ans += rem * rem *rem
        num = int(num /10)
    if ans == t:
        print(ans," Is Armstrong Number ")
    else:
        print(ans," Is Not Armstrong Number ")

def pali(num):
    t = num
    ans = 0
    while num != 0:
        rem = int(num % 10)
        ans = (ans * 10) + rem
        num = int(num / 10)

    if t == ans :
        print(t , " Is Palindrom Number ")
    else:
        print(t , " Is not Palindrom Number")
    

def rever(num):
    ans = 0
    while num != 0:
        rem = int(num % 10)
        ans = (ans * 10) + rem
        num = int(num / 10)
    return ans

def prime():
    num = int(input("Enter of Number : "))
    i = 2
    while i < num:
        if num%i == 0:
            return False
        i = i + 1
    return True


arm()
pali(101)
print(rever(123))
print(prime())
    
















