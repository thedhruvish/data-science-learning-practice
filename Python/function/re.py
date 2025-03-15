def table(n,i=1):
    if i == 11:
        return
    print(n," * ",i," = ",n*i)
    table(n,i+1)

table(5)
