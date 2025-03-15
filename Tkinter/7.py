from tkinter import * 

main = Tk()

main.title("My First GUI")
main.geometry("500x500")

tfram = Frame(main,width=250,height=250,bg='yellow')
tfram.pack(side='left')

btn1 = Button(tfram,text='miten',bg='red',border=2,fg='yellow')
btn1.place(x=26,y=30)


main.mainloop()
