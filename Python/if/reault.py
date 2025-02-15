rNo = int(input("Enter of Roll No : "))
name = input("Ente of Name : ")
sub1 = int(input("Enter of Subject 1 : "))
sub2 = int(input("Enter of Subject 2 : "))
sub3 = int(input("Enter of Subject 3 : "))
sub4 = int(input("Enter of Subject 4 : "))
sub5 = int(input("Enter of Subject 5 : "))

total = sub1 + sub2 + sub3 + sub4 + sub5

"""if sub1 > sub2 and sub1 > sub3 and sub1 > sub4 and sub1 > sub5:
    max = sub1
elif sub2 > sub3 and sub2 > sub4 and sub2 > sub5:
    max = sub2
elif sub3 > sub4 and sub3 > sub5:
    max = sub3
elif sub4 > sub5:
    max = sub4
else:
    max = sub5

if sub1 < sub2 and sub1 < sub3 and sub1 < sub4 and sub1 < sub5:
    min = sub1
elif sub2 < sub3 and sub2 < sub4 and sub2 < sub5:
    min = sub2
elif sub3 < sub4 and sub3 < sub5:
    min = sub3
elif sub4 < sub5:
    min = sub4
else:
    min = sub5
"""

max = max(sub1,sub2,sub3,sub4,sub5)
min = min(sub1,sub2,sub3,sub4,sub5)


c=0
if sub1 < 35:
    c = c + 1
if sub2 < 35:
    c = c + 1 
if sub3 < 35:
    c = c + 1
if sub4 < 35:
    c = c + 1
if sub5 < 35:
    c = c + 1 

if c == 0:
    reult = "pass"
elif c <= 2:
    reult = "ATKT"
else:
    reult = "Fail"



if reult == "Fail":
    pre = 0
else:
    pre = (sub1 + sub2 + sub3 + sub4 + sub5)/5


print("rNo\tName\tsub1\tsub2\tsub3\tsub4\tsub5\ttotal\tmin\tmax\tReualt\tPre")

print(rNo,"\t",name,"  ",sub1,"\t",sub2,"\t",sub3,"\t",sub4,"\t",sub5,"\t",total,"\t",min,"\t",max,"\t",reult,"\t",pre)

























