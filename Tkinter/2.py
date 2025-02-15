import tkinter as tk

main = tk.Tk()

main.geometry('400x400')
main.title("dhruvish")
btn1 = tk.Button(main,text='hello')
btn2 = tk.Button(main,text='new')
btn3 = tk.Button(main,text='login')
btn1.pack(side='left')
btn2.pack(side='right')
btn3.pack()
main.mainloop()