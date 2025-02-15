# Q4.How can we swap the values of three variables (let's say a, b, and c) without using a fourth 
# variable? For example, if we have a=5, b=8, and c=9, how can we obtain a=9, b=5, and c=8? The 
# challenge is to perform this operation without using an additional variable to store any of the values 
# during the swapping process. 


a = 5
b = 8
c = 9

a = a + b + c
b = a - (b + c) 
c = a - (b + c)  
a = a - (b + c) 


print("a =", a,"\nb =",b,"\nc=",c)
