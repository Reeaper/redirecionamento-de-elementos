from tkinter import *
# abre a janela
janela = Tk()
# muda o titulo
janela.title('Place')
# muda o icone
janela.iconbitmap('icons8-capivara-48.ico')
# tamanho da janela
janela.geometry('800x500+100+100')

# place dita as cordenadas do elemento em questao
btn1= Button(janela,text='Botão')
btn1.place(x=400,y=300)

btn2=Button(janela,text='Botão?')
btn2.place(x=300,y=400)

btn3=Button(janela,text='Botão!')
btn3.place(x=350,y=450)

caixa1=Entry(janela)
caixa1.place(x=50,y=150)

janela.mainloop()