from tkinter import *
def EnviarBD(MIN,MAX,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12):

    Algoritmo =


    print(Algoritmo)

    limpar()
    exibir()
    L_nome = Label(frameL, text='Produto enviado com sucesso', anchor=NE, font=('Ivy 8'), bg=co1, fg=co4)
    L_nome.place(x=75, y=220)

categoria = {1 : "Informática",2:"Alimentos",3:"Eletrônicos"}
def limpar():
    for widget in frameU.winfo_children():
        widget.destroy()
    for widget in frameL.winfo_children():
        widget.destroy()





# cores -----------------------------
co0 = "#000000"  # Preta / black
co1 = "#ffffff"  # branca / white
co2 = "#4169e1"  # Azul
co3 = "#38576b"  # valor / value
co4 = "#202020"  # letra / letters
verde = '#90f050'
azul_escuro = '#010012'
janela = Tk()
janela.title('')
janela.geometry('308x310')
janela.configure(background=co1)

janela.resizable(width=False, height=False)

# definindo frames

frameU = Frame(janela, width=308, height=50, bg=co1, relief='flat')
frameU.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frameL = Frame(janela, width=308, height=250, bg=co1, relief='flat')
frameL.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)



def hora(LinhaU,LinhaL):
    LinhaU.place(x=0, y=0)
    LinhaL.place(x=1000,y=0)
def umidade(LinhaU,LinhaL):
    LinhaU.place(x=0, y=1000)
    LinhaL.place(x=0, y=40)


def hora_umidade(LinhaU,LinhaL):
    LinhaU.place(x=1000, y=100)
    LinhaL.place(x=1000, y=0)
def exibir():
    global var
    global LinhaU
    global LinhaL
    # configurando frame superior
    L_nome = Label(frameU, text='Parametros irrigação', anchor=NE, font=('Ivy 23'), bg=co1, fg=co4)
    L_nome.place(x=10, y=5)

    L_linha = Label( text='', width=900, anchor=NE, font=('Ivy 1'), bg=co2, fg=co4)
    L_linha.place(x=0, y=45)

    # Configurando frame inferior
    LC = Label(frameL, text='Funcionar por: ', anchor=NW, font=('Ivy 12'), bg=co1, fg=co0, )
    LC.place(x=100, y=150)
    var = IntVar()
    C1 = Checkbutton(frameL, text='Horário', variable=var, onvalue=1, offvalue=0, command=lambda: hora(LinhaU,LinhaL),bg=co1, fg= co4)
    C1.place(x=10, y=173)
    C2 = Checkbutton(frameL, text='Umidade', variable=var, onvalue=2, offvalue=0, command=lambda: umidade(LinhaU,LinhaL),bg=co1, fg= co4)
    C2.place(x=95, y=173)
    C2 = Checkbutton(frameL, text='Umidade e Horário', variable=var, onvalue=3, offvalue=0, command=lambda: hora_umidade(LinhaU,LinhaL),bg=co1,fg= co4)
    C2.place(x=175, y=173)




    A_1 = Label(frameL, text='Qtd de água', anchor=NW, font=('Ivy 12'), bg=co1, fg=co4)
    A_1.place(x=0, y=10)
    H_1 = Label(frameL, text='Horário 1', anchor=NW, font=('Ivy 13'), bg=co1, fg=co4)
    H_1.place(x=10, y=43)
    H_2 = Label(frameL, text='Horário 2', anchor=NW, font=('Ivy 13'), bg=co1, fg=co4)
    H_2.place(x=10, y=78)
    H_3 = Label(frameL, text='Horário 3', anchor=NW, font=('Ivy 13'), bg=co1, fg=co4)
    H_3.place(x=10, y=113)
    H_linha = Label(text='', width=1,height=35, anchor=NE, font=('Ivy 2'), bg=co2, fg=co4)
    H_linha.place(x=90, y=50)
    H_linha = Label(frameL, text='', width=900, anchor=NE, font=('Ivy 1'), bg=co2, fg=co4)
    H_linha.place(x=0, y=140)
    H_linha = Label(text='', width=1,height=100, anchor=NE, font=('Ivy 2'), bg=co2, fg=co4)
    H_linha.place(x=305, y=50)
    H_linha = Label(text='', width=1,height=200, anchor=NE, font=('Ivy 1'), bg=co2, fg=co4)
    H_linha.place(x=-4, y=50)

    #####################################################################################################################
    A2 = Label(frameL, text='De:                % até               %', anchor=NW, font=('Ivy 11'), bg=co1, fg=co4)
    A2.place(x=101, y=10)
    MIN= Entry(frameL, width=6, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    MIN.place(x=142, y=10)
    MAX= Entry(frameL, width=6, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    MAX.place(x=237, y=10)




    L1 = Label(frameL, text='Inicio:      :       Final:       :', anchor=NW, font=('Ivy 11'), bg=co1, fg=co4)
    L1.place(x=101, y=43)
    E1 = Entry(frameL, width=2, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E1.place(x=142, y=43)
    E2= Entry(frameL, width=2, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E2.place(x=172, y=43)
    E3= Entry(frameL, width=2, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E3.place(x=237, y=43)
    E4 = Entry(frameL, width=2, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E4.place(x=267, y=43)

    L2 = Label(frameL, text='Inicio:      :       Final:       :', anchor=NW, font=('Ivy 11'), bg=co1, fg=co4)
    L2.place(x=101, y=78)
    E5 = Entry(frameL, width=2, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E5.place(x=142, y=78)
    E6= Entry(frameL, width=2, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E6.place(x=172, y=78)
    E7= Entry(frameL, width=2, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E7.place(x=237, y=78)
    E8 = Entry(frameL, width=2, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E8.place(x=267, y=78)

    L3 = Label(frameL, text='Inicio:      :       Final:       :', anchor=NW, font=('Ivy 11'), bg=co1, fg=co4)
    L3.place(x=101, y=113)
    E9= Entry(frameL, width=2, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E9.place(x=142, y=113)
    E10= Entry(frameL, width=2, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E10.place(x=172, y=113)
    E11= Entry(frameL, width=2, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E11.place(x=237, y=113)
    E12 = Entry(frameL, width=2, justify='left', font=('', 10), highlightthickness=1, relief='solid')
    E12.place(x=267, y=113)

    LinhaU =Label(frameL, text='', width=900, anchor=NE, font=('Ivy 1'),height=18, bg=azul_escuro)
    LinhaL =Label(frameL, text='', width=900, anchor=NE, font=('Ivy 1'),height=47, bg=azul_escuro)









    L_Button = Button(frameL, text='CONFIRMAR', width=38, height=2, bg=verde,
                      font=('Ivy 8 bold'), fg=co4, relief=RAISED, overrelief=RIDGE,
                      command=lambda: EnviarBD(MIN,MAX,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12))
    L_Button.place(x=15, y=200)

exibir()
janela.mainloop()