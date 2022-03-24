# class Teddy():
#     quantity=200
# teddy1=Teddy()
# print(teddy1.quantity)

class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name = input("Enter the Name:")
        self.mark=int(input("Enter the Mark:"))
    def putdetails(self):
        print(self.name,self.mark)
obj=student('name','mark')
obj.getdetails()
obj.putdetails()


