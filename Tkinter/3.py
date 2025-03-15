from tkinter import *  

main = Tk()

main.title('Login')
main.geometry('500x500')

name = Label(main,text='Enter of Name : ')
name.grid(row=0,column=0,pady=50,padx=50)
n1 =  Entry(main)
n1.grid(row=0,column=1)

btn = Button(main,text='Submit')
btn.grid(row=1,column=1)

main.mainloop()
