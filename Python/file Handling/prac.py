# f = open("demo.txt","r")
# print(f.read())

# # print(f.readline())
# # print(f.readline())
# f.close()

# f = open("demo1.txt",'w')
# f.write("hello word word")

# for i in f:
#     print(i)

f = open("demo1.txt","a")
f.write("hello word word")


import os
os.remove("demo.txt")