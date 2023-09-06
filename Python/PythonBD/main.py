from tkinter import *
import mysql.connector as bd

Bd = bd.connect(
    host="localhost",
    user="root",
    passwd ="",
    database="Py_BD"
)

cursor = Bd.cursor()
categoria = {1 : "Informática",2:"Alimentos",3:"Eletrônicos"}
def limpar():
    for widget in frameU.winfo_children():
        widget.destroy()
    for widget in frameL.winfo_children():
        widget.destroy()

def alterar():
    print()

def EnviarBD():

    insert = "insert into produtos(id,descricao,preco,categoria) values (%s,%s,%s,%s);"
    dados = E_1.get(), str(E_2.get()),E_3.get(),categoria.get(var.get())
    print(dados)

    cursor.execute(insert,dados)
    Bd.commit()

    limpar()
    exibir()
    L_nome = Label(frameL, text='Produto enviado com sucesso', anchor=NE, font=('Ivy 8'), bg=co1, fg=co4)
    L_nome.place(x=75, y=220)


# cores -----------------------------
co0 = "#000000"  # Preta / black
co1 = "#ffffff"  # branca / white
co2 = "#f00000"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"  # letra / letters
verde = '#90f050'

janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=co1)

janela.resizable(width=False, height=False)

# definindo frames

frameU = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frameU.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frameL = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frameL.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
def exibir():
    global E_1
    global E_2
    global E_3
    global var

    # configurando frame superior
    L_nome = Label(frameU, text='Cadastro de produtos', anchor=NE, font=('Ivy 23'), bg=co1, fg=co4)
    L_nome.place(x=5, y=5)

    L_linha = Label(frameU, text='', width=400, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    L_linha.place(x=0, y=45)

    # Configurando frame inferior
    L_1 = Label(frameL, text='Codigo *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    L_1.place(x=10, y=20)
    E_1 = Entry(frameL, width=25, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E_1.place(x=85, y=20)

    L_2 = Label(frameL, text='Descricao *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    L_2.place(x=10, y=60)
    E_2 = Entry(frameL, width=25, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E_2.place(x=85, y=60)

    L_3 = Label(frameL, text='Preço *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    L_3.place(x=10, y=100)
    E_3 = Entry(frameL, width=25, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E_3.place(x=85, y=100)

    var = IntVar()
    C1 = Checkbutton(frameL, text='Informática', variable=var, onvalue=1, offvalue=0, command=alterar,bg=co1)
    C1.place(x=10, y=140)
    C2 = Checkbutton(frameL, text='Alimentos', variable=var, onvalue=2, offvalue=0, command=alterar,bg=co1)
    C2.place(x=100, y=140)
    C2 = Checkbutton(frameL, text='Eletrônicos', variable=var, onvalue=3, offvalue=0, command=alterar,bg=co1)
    C2.place(x=185, y=140)

    L_Button = Button(frameL, text='CONFIRMAR', width=38, height=2, bg=verde,
                      font=('Ivy 8 bold'), fg=co4, relief=RAISED, overrelief=RIDGE, command=EnviarBD)
    L_Button.place(x=15, y=180)


exibir()
janela.mainloop()
