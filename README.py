from tkinter import*
import tkinter.messagebox
w1 = Tk()#สร้างหน้าต่างต่าง
w1.title("Menu")#ตั้งชื่อ
w1.geometry("450x600")#ขนาด
mylbel = Label(w1,text="สอบปลายภาค",fg="blue",bg="pink",font=("Tahoma",22)).pack()
mylbel = Label(w1,text="ม6/2",fg="blue",bg="pink",font=("Tahoma",22)).pack()
mylbel = Label(w1,text="").pack()
mylbel = Label(w1,text="ชื่อ...นาสกุล...",fg="blue",bg="pink",font=("Tahoma",22)).pack()
#ฟังก์ชันของ New file
def Newfile():
    w2 = Tk()
    w2.title("Open file")
    w2.geometry("450x450")
    mylbel = Label(w2,text="เข้ามาr?",fg="blue",bg="pink",font=("Tahoma",22)).pack()
    w2.mainloop()
def Open():
    tkinter.messagebox.showinfo("Open","เปิด***ไร")
def Save():
    tkinter.messagebox.showinfo("Save","บันทึก***ไร")
def Exit():
    con = tkinter.messagebox.askquestion("Exit","คุณต้องการออก?")
    if con == "yes":
        w1.destroy()
def Edit():
    tkinter.messagebox.showinfo("Edit","แก้ไข***ไร")
def About():
    tkinter.messagebox.showinfo("About Me","ชื่อmu")
#เมนูย่อย File
menuitem = Menu()
menuitem.add_command(label="New file",command=Newfile)
menuitem.add_command(label="Open ",command=Open)
menuitem.add_command(label="Save ",command=Save)
menuitem.add_command(label="Exit ",command=Exit)
#เมนูหลัก
mymenu = Menu()
w1.config(menu=mymenu)
mymenu.add_cascade(label="File",menu=menuitem)
mymenu.add_cascade(label="Edit",command=Edit)
mymenu.add_cascade(label="About",command=About)
w1.mainloop()
