from tkinter import *
janela=Tk()
janela.iconbitmap('icons8-capivara-48.ico')
janela.geometry('500x500+100+100')

lb1=Label(janela,bg='#FFE4E1',text='A')
lb1.pack(side=LEFT,fill=Y)

lb2=Label(janela,bg='#FFE4E1',text='B')
lb2.pack(side=TOP,fill=X)

lb3=Label(janela,bg='#FFE4E1',text='C')
lb3.pack(side=RIGHT,fill=Y)

lb4=Label(janela,bg='#FFE4E1',text='D')
lb4.pack(side=BOTTOM,fill=X)

janela.mainloop()