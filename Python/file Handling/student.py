f = open("Std.txt","w")
f.write("\tNo\tName\tsub1\tsub2\tsub3\tsub4\tsub5\ttotal\tavg")

def autoMark():
    import random
    return int(random.random() * 100)

n = int(input("Enter of Total Student : "))
israndom = bool(input("Can You Enter  Random Marks (True/False) Default True : "))
for i in range(n):
    print(f"\n*********** Student No {i+1} **************\n")
    name = input("Enter Name: ")
    if not israndom:
        sub1 = autoMark()
        sub2 = autoMark()
        sub3 = autoMark()
        sub4 = autoMark()
        sub5 = autoMark()
    else:
        sub1 = int(input("Enter of Subject 1 :"))
        sub2 = int(input("Enter of Subject 2 :"))
        sub3 = int(input("Enter of Subject 3 :"))
        sub4 = int(input("Enter of Subject 4 :"))
        sub5 = int(input("Enter of Subject 5 :"))

    total = sub1 + sub2 + sub3 + sub4 + sub5
    f.write(f"\n\t{i+1}\t{name}\t\t{sub1}\t\t{sub2}\t\t{sub3}\t\t{sub4}\t\t{sub5}\t\t{total}\t\t{total/5}")

isprint = bool(input("Can you Print Student Reualt Here (True/False) Default True : "))
if not isprint:
    f.close()
    f = open("Std.txt","r")
    print(f.read())
f.close()

print(" 😎 Student Details are save 😎 ")


