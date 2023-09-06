from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from imovel import Imovel
from endereco import Endereco

CREDENCIAIS = ['Guilherme', '123']
Edificios = []
def verificalogin():
    nome = E_nome.get()
    senha = E_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin')
    elif nome == CREDENCIAIS[0] and CREDENCIAIS[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta')
        limpar()
        JanelaDados()
    else:
        messagebox.showwarning('ERROR', 'Verifique o nome e a senha')


def limpar():
    for widget in frameU.winfo_children():
        widget.destroy()
    for widget in frameL.winfo_children():
        widget.destroy()

def alterarC():
    print()

def alterarAP():
    print()

def enviaDados():
    comodos = E1.get()
    valor = E2.get()
    areacontruida = E5.get()
    tipo = var
    rua = E3.get()
    CEP = E4.get()
    cidade = E6.get()
    bairro = E7.get()
    End = Endereco(cidade, bairro, rua, CEP)
    IM = Imovel(areacontruida,comodos,tipo,End,valor)
    Edificios.append(IM)
    print(Edificios)
def JanelaDados():
    L_nome = Label(frameU, text='Usuário : ' + CREDENCIAIS[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    L_nome.place(x=5, y=5)
    L_linha = Label(frameU, text='', width=250, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    L_linha.place(x=10, y=45)

    global E1, E2, E3, E4, E5, E6, E7, var


    L1 = Label(frameL, text='Quantidade de comodos: *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    L1.place(x=10, y=15)
    E1 = Entry(frameL, width=20, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E1.place(x=14, y=35)

    L2 = Label(frameL, text='Valor: *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    L2.place(x=170, y=15)
    E2 = Entry(frameL, width=10, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E2.place(x=170, y=35)

    L3 = Label(frameL, text='Logradouro  *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    L3.place(x=10, y=60)
    E3 = Entry(frameL, width=20, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E3.place(x=14, y=80)

    L4 = Label(frameL, text='CEP *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    L4.place(x=170, y=60)
    E4 = Entry(frameL, width=10, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E4.place(x=170, y=80)

    L5 = Label(frameL, text='Area Construida: *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    L5.place(x=10, y=105)
    E5 = Entry(frameL, width=15, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E5.place(x=14, y=125)

    L6 = Label(frameL, text='Cidade *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    L6.place(x=130, y=105)
    E6 = Entry(frameL, width=8, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E6.place(x=130, y=125)

    L7 = Label(frameL, text='Bairro *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    L7.place(x=200, y=105)
    E7 = Entry(frameL, width=8, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E7.place(x=200, y=125)

    var = IntVar()
    C1 = Checkbutton(frameL, text='Casa', variable=var, onvalue=1, offvalue=0, command=alterarC)
    C1.place(x=10,y=150)
    C2 = Checkbutton(frameL, text='Apartamento', variable=var, onvalue=0, offvalue=1, command=alterarAP)
    C2.place(x=150, y=150)


    L_Button = Button(frameL, text='CONFIRMAR', width=38, height=2, bg=verde,
                      font=('Ivy 8 bold'), fg=co4, relief=RAISED, overrelief=RIDGE, command=enviaDados)
    L_Button.place(x=15, y=180)


# cores -----------------------------
co0 = "#000000"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"  # letra / letters
verde = '#00f000'

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

# configurando frame superior
L_nome = Label(frameU, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
L_nome.place(x=5, y=5)

L_linha = Label(frameU, text='', width=250, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
L_linha.place(x=10, y=45)

# Configurando frame inferior
L_nome = Label(frameL, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
L_nome.place(x=10, y=20)
E_nome = Entry(frameL, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
E_nome.place(x=14, y=50)

L_pass = Label(frameL, text='Senha *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
L_pass.place(x=10, y=95)
E_pass = Entry(frameL, width=25, show='*', justify='left', font=('', 15), highlightthickness=1, relief='solid')
E_pass.place(x=14, y=130)

L_Button = Button(frameL, text='CONFIRMAR', width=38, height=2, bg=verde,
                  font=('Ivy 8 bold'), fg=co4, relief=RAISED, overrelief=RIDGE, command=verificalogin)
L_Button.place(x=15, y=180)

janela.mainloop()

