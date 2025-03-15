
"""
list1 = []
for i in range(0,5):
    a = int(input("Enter of Value : "))
    list1.append(a)



ansSum = 0

for i in list1:
    ansSum = i + ansSum


print("Total Sum ",ansSum)
"""
# input list
lst = [10, 11, 12, 13, 14, 15]
# the above input can also be given as
# lst=list(map(int,input().split()))
l = []  # empty list

# iterate to reverse the list
for i in lst:
    # reversing the list
    l.insert(0, i)
# printing result
print(l)
