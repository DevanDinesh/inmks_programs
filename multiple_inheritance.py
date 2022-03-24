class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("Enter your name:")
        self.mark=int(input("Enter your Mark:"))
    def putd(self):
        print(self.name,self.mark)
class teacher(Student):
    def display(self):
        print("am Derrived class1")
class parent(teacher):
    def newfun(self):
        print("am Derrived class2")

obj=parent('teacher','student')
obj.getdetails()
obj.putd()
obj.display()
obj.newfun()
