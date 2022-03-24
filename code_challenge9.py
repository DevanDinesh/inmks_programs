class Computer:
    def __init__(self, ram, gpu):
        self.ram = ram
        self.gpu = gpu
    def getspecs(self):
        print("Enter specifications")
        self.ram = input("Enter RAM size: ")
        self.gpu = input("Enter GPU model: ")
    def displayspecs(self):
        print("Specifications of your system")
        print("Ram size:{} GPU:{}".format(self.ram, self.gpu))
class Desktop(Computer):
    def __init__(self, company):
        self.company = company
    def getcompany(self):
        self.company = input("Enter company: ")
    def showcompany(self):
        print("Desktop specifications")
        print("Company:{}".format(self.company))
class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight
    def getweight(self):
        self.weight = input("Enter weight: ")
    def showweight(self):
        print("Laptop weight")
        print("Laptop weight:{}".format(self.weight))
object1 = Laptop("")
object1.getspecs()
object1.getweight()
object1.displayspecs()
object1.showweight
