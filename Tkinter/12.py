from tkinter import * 


def getNumber(n):
    print(n)
    entry.insert(END, n) 



main = Tk()
main.geometry("400x500")
main.title("Calculator")
entry = Entry(main, font=('Helvetica', 16))
entry.grid(row=1, column=0, columnspan=4)




Button(main,text='1',command=lambda : getNumber(1),padx=20,pady=20  ).grid(row=3,column=1)
Button(main,text='2',command=lambda : getNumber(2),padx=20,pady=20, ).grid(row=3,column=2)
Button(main,text='3',command=lambda : getNumber(3),padx=20,pady=20, ).grid(row=3,column=3)
Button(main,text='4',command=lambda : getNumber(4),padx=20,pady=20, ).grid(row=4,column=1)
Button(main,text='5',command=lambda : getNumber(5),padx=20,pady=20, ).grid(row=4,column=2)
Button(main,text='6',command=lambda : getNumber(6),padx=20,pady=20, ).grid(row=4,column=3)
Button(main,text='7',command=lambda : getNumber(7),padx=20,pady=20, ).grid(row=5,column=1)
Button(main,text='8',command=lambda : getNumber(8),padx=20,pady=20, ).grid(row=5,column=2)
Button(main,text='9',command=lambda : getNumber(9),padx=20,pady=20, ).grid(row=5,column=3)


main.mainloop()