from tkinter import *

main = Tk()
main.geometry('400x500')
main.title('My Calculator')
l = []
def cala(l):
    try:
        num = []
        exp = []

        current_number = ""

        for item in l:
            item = str(item)
            if item.isdigit():
                current_number += item
            else:
                if current_number:
                    num.append(int(current_number))
                    current_number = ""
                exp.append(item)

        if current_number:
            num.append(int(current_number))

        ans = int(num[0])
        for i in range(len(exp)):
            if exp[i] == '*':
                ans = int(ans) * int(num[i+1])
            elif exp[i] == '-':
                ans = int(ans) - int(num[i+1])
            elif exp[i] == '+':
                ans = int(ans) + int(num[i+1])
            elif exp[i] == '/':
                ans = int(ans) / int(num[i+1])

        return str(ans)

    except Exception as ex:
        return ex

def button_click(val):
    if val == '=':
        entry.delete(0, END)
        ans = cala(l)
        entry.insert(0, ans)
        l.clear()
        l.append(ans)
    elif val == 'C':
        l.clear()
        entry.delete(0, END)
    elif val == 'CE':
        current = entry.get()
        if current:
            entry.delete(len(current) - 1, END)
            if l:
                l.pop()
    else:
        entry.insert(END, val)
        l.append(val)

entry = Entry(main, font=('Helvetica', 30),justify='right')
entry.grid(row=0, column=0, columnspan=4,sticky='nsew')


Button(main,text='/',command=lambda : button_click('/')).grid(row=1, column=0,sticky='nsew')  
Button(main,text='-',command=lambda : button_click('-')).grid(row=1, column=1,sticky='nsew')  
Button(main,text='CE',command=lambda : button_click('CE')).grid(row=1, column=2,sticky='nsew')  
Button(main,text='C',command=lambda : button_click('C'),bg='red').grid(row=1, column=3,sticky='nsew')

Button(main,text='7',command=lambda : button_click(7)).grid(row=2, column=0,sticky='nsew') 
Button(main,text='8',command=lambda : button_click(8)).grid(row=2, column=1,sticky='nsew') 
Button(main,text='9',command=lambda : button_click(9)).grid(row=2, column=2,sticky='nsew') 
Button(main,text='*',command=lambda : button_click('*')).grid(row=2,column=3,sticky='nsew')


Button(main,text='4',command=lambda : button_click(4)).grid(row=3, column=0,sticky='nsew')  
Button(main,text='5',command=lambda : button_click(5)).grid(row=3, column=1,sticky='nsew')  
Button(main,text='6',command=lambda : button_click(6)).grid(row=3, column=2,sticky='nsew')  
Button(main,text='+',command=lambda : button_click('+')).grid(row=3,column=3,rowspan=2,sticky='nsew') 

Button(main,text='1',command=lambda : button_click(1)).grid(row=4,  column=0,sticky='nsew')
Button(main,text='2',command=lambda : button_click(2)).grid(row=4,  column=1,sticky='nsew')
Button(main,text='3',command=lambda : button_click(3)).grid(row=4,  column=2,sticky='nsew')

Button(main,text='C',command=lambda : button_click('C')).grid(row=5, column=0,sticky='nsew') 
Button(main,text='0',command=lambda : button_click(0)).grid(row=5, column=1,sticky='nsew') 
Button(main,text='=',command=lambda : button_click('=')).grid(row=5, column=2,columnspan=2,sticky='nsew') 




for i in range(6): 
    main.grid_rowconfigure(i, weight=1)
for j in range(4): 
    main.grid_columnconfigure(j, weight=1)

main.mainloop()