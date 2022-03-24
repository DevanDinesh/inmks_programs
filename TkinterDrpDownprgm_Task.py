from tkinter import *
root=Tk()
def fun():
    print("This is New Project")
def fun1():
    print("This is New File")
def fun2():
    print("This is open File")
def fun3():
    print("This is Save As")
def fun4():
    print("This is Open Recent")


def fun5():
    print("This is Undo Typing")
def fun6():
    print("This is Cut")
def fun7():
    print("This is Copy")
def fun8():
    print("This is Paste")
def fun9():
        print("This is Delete")
def fun10():
        print("This is Find")


def fun11():
        print("This is Tool Windows")
def fun12():
        print("This is Appearance")
def fun13():
        print("This is Quick Definition")
def fun14():
        print("This is Quick Type Definition")
def fun15():
        print("This is Quick Documentation")
def fun16():
    print("This is Parameter Info")


def fun17():
        print("This is Back")
def fun18():
        print("This is class")
def fun19():
    print("This is file")
def fun20():
        print("This is symbol")
def fun21():
    print("This is Line:column")
def fun22():
    print("This is select In")

def fun23():
    print("This is Generate")
def fun24():
    print("This is Code_completion")
def fun25():
    print("This is Inspect code")
def fun26():
    print("This is Code cleanup")
def fun27():
    print("This is Analyze code")
def fun28():
    print("This is Surround with")



def fun29():
    print("This is Refactor This")
def fun30():
    print("This is Rename")
def fun31():
    print("This is Change Signature")
def fun32():
    print("This is Extract")
def fun33():
    print("This is Copy File")
def fun34():
    print("This is Move File")


mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New project",command=fun)
submenu.add_command(label="New",command=fun1)
submenu.add_separator()
submenu.add_command(label="open",command=fun2)
submenu.add_command(label="Save As",command=fun3)
submenu.add_separator()
submenu.add_command(label="Open Recent",command=fun4)
submenu.add_command(label="Exit",command=exit)

newmenu=Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=newmenu)
newmenu.add_command(label="Undo Typing",command=fun5)
newmenu.add_command(label="Cut",command=fun6)
newmenu.add_separator()
newmenu.add_command(label="Copy",command=fun7)
newmenu.add_command(label="Paste",command=fun8)
newmenu.add_separator()
newmenu.add_command(label="Delete",command=fun9)
newmenu.add_command(label="Find",command=fun10)

newmenu=Menu(mymenu)
mymenu.add_cascade(label="View",menu=newmenu)
newmenu.add_command(label="Tool Windows",command=fun11)
newmenu.add_command(label="Appearance",command=fun12)
newmenu.add_separator()
newmenu.add_command(label="Quick Definition",command=fun13)
newmenu.add_command(label="Quick Type Definition",command=fun14)
newmenu.add_separator()
newmenu.add_command(label="Quick Documentation",command=fun15)
newmenu.add_command(label="Parameter Info",command=fun16)

newmenu=Menu(mymenu)
mymenu.add_cascade(label="Navigate",menu=newmenu)
newmenu.add_command(label="Back",command=fun17)
newmenu.add_command(label="Class",command=fun18)
newmenu.add_separator()
newmenu.add_command(label="File",command=fun19)
newmenu.add_command(label="Symbol",command=fun20)
newmenu.add_separator()
newmenu.add_command(label="Line:column",command=fun21)
newmenu.add_command(label="Select In",command=fun22)

newmenu=Menu(mymenu)
mymenu.add_cascade(label="Code",menu=newmenu)
newmenu.add_command(label="Generate",command=fun23)
newmenu.add_command(label="Code_completion",command=fun24)
newmenu.add_separator()
newmenu.add_command(label="Inspect code",command=fun25)
newmenu.add_command(label="Code cleanup",command=fun26)
newmenu.add_separator()
newmenu.add_command(label="Analyze code",command=fun27)
newmenu.add_command(label="Surround with",command=fun28)

newmenu=Menu(mymenu)
mymenu.add_cascade(label="Refactor",menu=newmenu)
newmenu.add_command(label="Refactor This",command=fun29)
newmenu.add_command(label="Rename",command=fun30)
newmenu.add_separator()
newmenu.add_command(label="Change Signature",command=fun31)
newmenu.add_command(label="Extract",command=fun32)
newmenu.add_separator()
newmenu.add_command(label="Move File",command=fun33)
newmenu.add_command(label="Copy File",command=fun34)
root.mainloop()