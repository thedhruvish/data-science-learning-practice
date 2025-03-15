from tkinter import * 

main = Tk()

btn1 = Button(main,text='hello' ,bg='red',fg='blue',width=100)
btn1.pack(side='bottom')

check = Checkbutton(main,text='Green')
check.pack(side='bottom')

main.mainloop()