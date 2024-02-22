from tkinter import *

janela=Tk()
janela.iconbitmap('icons8-capivara-48.ico')
janela.geometry('500x500+100+100')

lb1=Label(janela,
    bg='purple',
    text='fill=X')
lb1.pack(fill=X)   

lb2=Label(janela,
    bg='pink',
    text='expand=0')
lb2.pack(expand=0,side=LEFT)   

lb3=Label(janela,
    bg='#FFE4E1',
    text='A esquerda,fill=Y')
lb3.pack(fill=Y,side=LEFT)   

lb4=Label(janela,
    bg='#B0E0E6',
    text='fill=BOTH')
lb4.pack(fill=BOTH)   

lb5=Label(janela,
    bg='#D8BFD8',
    text='expand=1,fill=BOTH')
lb5.pack(expand=1,fill=BOTH)   


janela.mainloop()