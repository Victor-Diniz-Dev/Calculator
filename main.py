from tkinter import *

root = Tk()
root.title('Calculadora')
root.geometry('493x380')
root.minsize(493, 380)
root.maxsize(493, 380)

numero1 = ''
div = FALSE 
multiplica = FALSE
subtrai = FALSE
adicao = FALSE

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)

def botao_click(num):
    e.insert(END, num)

def botao_div():
    global numero1
    global div
    div = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_multiplica():
    global numero1
    global multiplica
    multiplica = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_subtrai():
    global numero1
    global subtrai
    subtrai = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_adicao():
    global numero1
    global adicao
    adicao = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_limpa():
    e.delete(0, END)

def botao_igual():
    global adicao
    global subtrai
    global div
    global multiplica
    numero2 = e.get()
    e.delete(0, END)
    
    if adicao == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        adicao = FALSE
    if multiplica == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplica = FALSE
    if div == TRUE:
        e.insert(0, int(numero1) / int(numero2))
        div = FALSE
    if subtrai == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtrai = FALSE

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

divide.grid(row=0, column=4)
#primeira fileira
um = Button(root,
                text='1',
                padx=40,
                pady=20,
                command=lambda: botao_click(1),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064', 
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
um.grid(row=1, column=1)

dois = Button(root,
                text='2',
                padx=40,
                pady=20,
                command=lambda: botao_click(2),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
dois.grid(row=1, column=2)

tres = Button(root,
                text='3',
                padx=40,
                pady=20,
                command=lambda: botao_click(3),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
tres.grid(row=1, column=3)

botao_multiplica = Button(root,
                text='x',
                padx=40,
                pady=20,
                command=botao_multiplica,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
botao_multiplica.grid(row=1, column=4)

#segunda fileira
quatro = Button(root,
                text='4',
                padx=40,
                pady=20,
                command=lambda: botao_click(4),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
quatro.grid(row=2, column=1)

cinco = Button(root,
                text='5',
                padx=40,
                pady=20,
                command=lambda: botao_click(5),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
cinco.grid(row=2, column=2)

seis = Button(root,
                text='6',
                padx=40,
                pady=20,
                command=lambda: botao_click(6),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
seis.grid(row=2, column=3)

menos = Button(root,
                text='-',
                padx=41.5,
                pady=20,
                command=botao_subtrai,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
menos.grid(row=2, column=4)

#terceira fileira
sete = Button(root,
                text='7',
                padx=40,
                pady=20,
                command=lambda: botao_click(7),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
sete.grid(row=3, column=1)

oito = Button(root,
                text='8',
                padx=40,
                pady=20,
                command=lambda: botao_click(8),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
oito.grid(row=3, column=2)

nove = Button(root,
                text='9',
                padx=40,
                pady=20,
                command=lambda: botao_click(9),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
nove.grid(row=3, column=3)

adicao = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_adicao,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
adicao.grid(row=3, column=4)

#quarta fileira

zero = Button(root,
                text='0',
                padx=101.5,
                pady=20,
                command=lambda: botao_click(0),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
zero.grid(row=4, column=1, columnspan=2)

limpa = Button(root,
                text='C',
                padx=40,
                pady=20,
                command=botao_limpa,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
limpa.grid(row=4, column=4)

igual = Button(root,
                text='=',
                padx=40,
                pady=20,
                command=botao_igual,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
igual.grid(row=4, column=3)

root.mainloop()