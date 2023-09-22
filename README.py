from tkinter import*
import tkinter.messagebox
w1 = Tk()
w1.title("Menu")
w1.geometry("600x600")
def Openfile():
    w2 = Tk()
    w2.title("Openfile")
    w2.geometry("450x450")
    mylable = Label(w2,text="หน้านี้คือหน้าต่างใหม่").pack()
    w2.mainloop()
def Savefile():
    tkinter.messagebox.showinfo("Savefile","คุณต้องการจะเซฟไฟล์หรือไม่")
def Exitprogram():
    BB = tkinter.messagebox.askquestion("Exitprogram","คุณต้องการจะออกจากโปรแกรมหรือไม่")
    if BB == "yes":
        w1.destroy()
#small menu
NN = Menu()
NN.add_command(label="Openfile",command=Openfile)
NN.add_command(label="Save",command=Savefile)
NN.add_command(label="Exit",command=Exitprogram)
#main menu
MM = Menu()
w1.config(menu=MM)
MM.add_cascade(label="File",menu=NN)
MM.add_cascade(label="Edit")
MM.add_cascade(label="Aboutme")
w1.mainloop()
