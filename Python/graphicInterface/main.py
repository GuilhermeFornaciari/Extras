from tkinter  import *
from tkinter import  ttk

cor1 = "#000000"
cor2 = "#ffffff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"
janela= Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

#frames
frame_tela = Frame(janela, width=235,height=50, bg=cor3)
frame_tela.grid(row=0,column=0)

frame_corpo = Frame(janela,width=235,height=268)
frame_corpo.grid(row=1,column=0)

#botoes
b_1 = Button(frame_corpo,text="C",width=11,height=2)
b_1.place(x=0,y=0)


janela.mainloop()