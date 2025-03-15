from tkinter import * 

main = Tk()
main.geometry('300x400')
lb1 = Label(main,text='Enter of Name')
lb1.place(x=10,y=20)
lb2 = Label(main,text='Enter of Age')
lb2.place(x=10,y=60)

lb = Listbox(main,height=5)
lb.insert(1,'red')
lb.insert(2,'red')
lb.insert(3,'red')
lb.insert(4,'red')
lb.insert(5,'red')
lb.place(x=10,y=100)


rdb = Radiobutton(main,text='red',variable='radio',value=1)
rdb.pack()

lb1 = Label(main,text='Enter of Address')
lb1.place(x=100,y=200)
txt = Text(main,width=15,height=5)
txt.place(x=120,y=220)

s = Scale(main,from_=100,to=200,orient='horizontal')
s.place(x=130,y=230)

def fun():
    child = Toplevel(main)
    child.mainloop()
btn1 = Button(main,text='Entere',width=10,command=fun)
btn1.place(x=350,y=350)




main.mainloop()