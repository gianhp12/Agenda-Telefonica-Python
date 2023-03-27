from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox


# cores ---------

co0 = "#f0f3f5"  # Preta
co1 = "#E0E0EE"  # cinzenta / grey
co2 = "#feffff"  # branca
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#6f9fbd"  # azul
co6 = "#ef5350"  # vermelha
co7 = "#93cd95"  # verde

# criando janela -----
janela = Tk ()
janela.title ("")
janela.geometry('500x450')
janela.configure(background=co1);
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# frames

frame_cima = Frame(janela,width=500,height=50,bg=co3,relief="flat")
frame_cima.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)

frame_baixo = Frame(janela,width=500,height=150,bg=co1,relief="flat")
frame_baixo.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)

frame_tabela = Frame(janela,width=500,height=248,bg=co2,relief="flat")
frame_tabela.grid(row=2,column=0,columnspan=2,padx=10,pady=1,sticky=NW)



janela.mainloop()
