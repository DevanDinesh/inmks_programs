from tkinter import *
from tkinter import messagebox
root=Tk()
messagebox.showinfo('Welcome',"This is here ")
messagebox.showwarning('title',"This is Warning")
messagebox.showerror('title',"This is error")
messagebox.askquestion('title',"Are you want to exit")
messagebox.askokcancel('title',"Are you sure?")
messagebox.askyesno('title',"Are you ok")
messagebox.askretrycancel('title',"Are you ok")

root.mainloop()