from tkinter import*
import tkinter.messagebox
w1 = Tk()
w1.geometry("450x450")
w1.title("Menu")
mylabel1 = Label(w1,text="Hello Wrold").pack()
def Menu1_1():
    w2 = Tk()
    w2.title("Menu1.1")
    w2.geometry("400x400")
    lable =Label(w2,text="1.1").pack()
    w2.mainloop()

def Menu1_2():
    w3 = Tk()
    w3.title("Menu1.2")
    w3.geometry("400x400")
    lable =Label(w3,text="1.2").pack()
    w3.mainloop()

def Menu2_1():
    w4 = Tk()
    w4.title("Menu2.1")
    w4.geometry("400x400")
    la =Label(w4,text="2.1").pack()  
    w4.mainloop()

def Menu2_2():
    w5 = Tk()
    w5.title("Menu2.2")
    w5.geometry("400x400")
    la =Label(w5,text="2.2").pack()
    w5.mainloop()

def Aboutme():
    tkinter.messagebox.showinfo("Design by","xxxxx")

def Exitprogram():
    con = tkinter.messagebox.askquestion("Exit program","คุณต้องการออกจากโปรแกรมใช่หรือไม่")
    if con == "yes":
        w1.destroy()

#small menu
menuitem1 = Menu()
menuitem1.add_command(label="Menu1.1",command=Menu1_1)
menuitem1.add_command(label="Menu1.2",command=Menu1_2)
menuitem2 = Menu()
menuitem2.add_command(label="Menu2.1",command=Menu2_1)
menuitem2.add_command(label="Menu2.2",command=Menu2_2)
#mainmenu
mymenu = Menu()
w1.config(menu=mymenu)
mymenu.add_cascade(label="Menu1",menu=menuitem1)
mymenu.add_cascade(label="Menu2",menu=menuitem2)
mymenu.add_cascade(label="About me",command=Aboutme)
mymenu.add_cascade(label="Exit",command=Exitprogram)
w1.mainloop()
