from tkinter import *

main = Tk()
main.geometry('400x500')
main.title('Tic Tac Toe')
x = [0,0,0,0,0,0,0,0,0]
y = [0,0,0,0,0,0,0,0,0]
labelResult = Label(main, text="0 Trun", font=('Roboto', 16))
labelResult.grid(row=0, column=0, columnspan=4)
tn = 0
btns = [] 

def reset_btn(win=False):
    global tn
    if win:
        for i in range(9):
            btns[i].config(state='disable')
        return
    for i in range(9):
        btns[i].config(text='',state='normal')
        x[i] = y[i] = 0
    tn = 0
    labelResult.config(text='0 Trun',background='white')

def check_win():
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8],[0, 4, 8],[2, 4, 6]]
    for i in winning_combinations:
        if x[i[0]] == x[i[1]] == x[i[2]] == 1:
            labelResult.config(text='X Win',background='yellow',font=('Roboto', 30))
            reset_btn(True)
            return
        elif y[i[0]] == y[i[1]] == y[i[2]] == 1:
            labelResult.config(text='0 Win',background='yellow',font=('Roboto', 30))
            reset_btn(True)
            return
    if tn == 9:
        labelResult.config(text='Game Over',background='red',font=('Roboto', 30))

def click_btn(val):
    global tn
    print(tn)
    if int(tn%2):
        x[val] = 1
        btns[val].config(text='X',state='disabled')
        tn += 1
        labelResult.config(text='0 Trun')
    else:
        y[val] = 1
        btns[val].config(text='0',state='disabled')
        tn += 1
        labelResult.config(text='X Trun')
    check_win()
    

for i in range(9):
    btn = Button(main, text='', command=lambda i=i: click_btn(i),font=('Roboto', 30))
    btn.grid(row=(i//3)+1, column=i%3, sticky='nsew')
    btns.append(btn)

re_btn = Button(main, text="Reset Game", font=('Roboto', 20), command=reset_btn)
re_btn.grid(row=4, column=0, columnspan=3)


for i in range(5): 
    main.grid_rowconfigure(i, weight=1)
for j in range(3): 
    main.grid_columnconfigure(j, weight=1)

main.mainloop()