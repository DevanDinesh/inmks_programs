from tkinter import *
root=Tk()
l1=Label(root,text="Username",fg="black",bg="red")
l2=Label(root,text="Password",fg="black",bg="red")
# l3=Label(root,text="password again")
entry1=Entry(root)
entry2=Entry(root)

l1.grid(row=0,column=0)
entry1.grid(row=0,column=1)
l2.grid(row=1,column=0)
entry2.grid(row=1,column=1)
root.mainloop()