from tkinter import *

root = Tk()

root.title('Calculadora')
root.geometry('408x355')
root.minsize(408,355)
root.maxsize(408, 355)
root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#A7A28F', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)

def botao_div():
    return    

divide = Button(root,
                text='÷',
                padx=40,
                pady=20,
                command=botao_div,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)

divide.grid(row=0, 
            column=4
)

root.mainloop()