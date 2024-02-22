from tkinter import *
# abre a janela
janela = Tk()
# muda o titulo
janela.title('Anchor')
# muda o icone
janela.iconbitmap('icons8-capivara-48.ico')
# tamanho da janela
janela.geometry('800x500+100+100')

# anchor dita as cordenadas com pontos cardeais no elemento em questao
btn1= Button(janela,text='Botão')
btn1.place(x=400,y=300,anchor=NE)

btn2=Button(janela,text='Botão?')
btn2.place(x=300,y=400,anchor=E)

btn3=Button(janela,text='Botão!')
btn3.place(x=350,y=450,anchor=NW)

caixa1=Entry(janela)
caixa1.place(x=50,y=150,anchor=W)

janela.mainloop()