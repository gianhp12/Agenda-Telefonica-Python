from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox


# cores ---------

co0 = "#f0f3f5"  # Preta
co1 = "#BDBDB7"  # cinzenta / grey
co2 = "#feffff"  # branca
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#6f9fbd"  # azul
co6 = "#ef5350"  # vermelha
co7 = "#93cd95"  # verde
co8 = "#DCDC14"  #amarelo
# criando janela -----
janela = Tk ()
janela.title ("")
janela.geometry('500x450')
janela.configure(background=co1);
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# frames

frame_up = Frame(janela,width=500,height=50,bg=co3,relief="flat")
frame_up.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)

frame_down = Frame(janela,width=500,height=150,bg=co1,relief="flat")
frame_down.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)

frame_table = Frame(janela,width=500,height=248,bg=co2,relief="flat")
frame_table.grid(row=2,column=0,columnspan=2,padx=10,pady=1,sticky=NW)

# label

l_title = Label(frame_up,text='Agenda Telefônica',anchor=NE,font=('arial 20 bold'),bg=co3,fg=co2)
l_title.place(x=5,y=5)

#linha de divisão com frame
l_line = Label(frame_up,width=500,anchor=NE,font=('arial 1'),bg=co2,fg=co1)
l_line.place(x=0,y=46)

#labels e text fields do frame baixo
l_name = Label(frame_down,text='Nome *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4)
l_name.place(x=10,y=20)
e_name = Entry(frame_down, width=25, justify='left',font=('',10),highlightthickness=1)
e_name.place(x=80, y=20)

l_gender = Label(frame_down,text='Sexo *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4)
l_gender.place(x=10,y=50)
c_gender = Combobox(frame_down,width=27)
c_gender['value'] = ('','Feminino','Masculino')
c_gender.place(x=80,y=50)

l_telphone = Label(frame_down,text='Telefone *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4)
l_telphone.place(x=10,y=80)
e_telphone = Entry(frame_down, width=25, justify='left',font=('',10),highlightthickness=1)
e_telphone.place(x=80, y=80)

l_email = Label(frame_down,text='Email *',anchor=NW,font=('Ivy 10 bold'),bg=co1,fg=co4)
l_email.place(x=10,y=110)
e_email = Entry(frame_down, width=25, justify='left',font=('',10),highlightthickness=1)
e_email.place(x=80, y=110)

b_find = Button(frame_down,text='Procurar',font=('Ivy 8 bold'),bg=co5,fg=co2,relief=RAISED,overrelief=RIDGE)
b_find.place(x=430,y=20)
e_find = Entry(frame_down, width=20, justify='left',font=('',10),highlightthickness=1)
e_find.place(x=280, y=20)

b_viewdata = Button(frame_down,text='Ver dados',font=('Ivy 8 bold'),bg=co5,fg=co2,relief=RAISED,overrelief=RIDGE)
b_viewdata.place(x=430,y=50)

b_add = Button(frame_down,text='Adicionar',font=('Ivy 8 bold'),bg=co7,fg=co2,relief=RAISED,overrelief=RIDGE)
b_add.place(x=280,y=50)

b_edit = Button(frame_down,text='Atualizar',font=('Ivy 8 bold'),bg=co8,fg=co2,relief=RAISED,overrelief=RIDGE)
b_edit.place(x=280,y=80)

b_delete = Button(frame_down,text='Deletar',font=('Ivy 8 bold'),bg=co6,fg=co2,relief=RAISED,overrelief=RIDGE)
b_delete.place(x=280,y=110)

janela.mainloop()
