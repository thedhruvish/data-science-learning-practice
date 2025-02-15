import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active
def autoMark():
  import random
  return int(random.random() * 100)

sheet.append( ["No","Name","sub1","sub2","sub3","sub4","sub5","total","avg"])
temp = []
n = int(input("Enter of Total Student : "))
israndom = bool(input("Can You Enter  Random Marks (True/False) Default True : ")) and True

for i in range(n):  
  print(f"\n*********** Student No {i+1} **************\n")
  temp.append(i+1)
  temp.append(input("Enter Name: "))
  
  if not israndom:
    for x in range(0,5):
      temp.append(int(autoMark()))
  else:
    for x in range(0,5):
      temp.append(int(input(f"Enter Marks of Subject {x+1} : ")))
  
  mark_sum = sum(temp[2:])    
  temp.append(mark_sum)
  temp.append(mark_sum/5)

  sheet.append(temp)
  temp.clear()
  
workbook.save("student.xlsx")
