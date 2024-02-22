from tkinter import *
# abre a janela
janela = Tk()
# muda o titulo
janela.title('Grid')
# muda o icone
janela.iconbitmap('icons8-capivara-48.ico')
# tamanho da janela
janela.geometry('500x250+100+100')

lb1=Label(janela,text='Login')
lb1.grid(column=0,row=0)

lb2=Label(janela,text='Senha')
lb2.grid(column=0,row=1,
         padx=(15,15),
         pady=(15,15))

en1=Entry(janela)
en1.grid(column=1,row=0)

en2=Entry(janela)
en2.grid(column=1,row=1)

btn1=Button(janela,text='Enviar')
# columnspan e rowspan serve para mesclar colunas e linhas,respectivamente
btn1.grid(columnspan=2,rowspan=3)

janela.mainloop()