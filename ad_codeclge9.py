class hospital:
    def __init__(self,admin,doctor,sister,department):
        self.admin=admin
        self.doctor = doctor
        self.sister = sister
        self.department = department
    def getdetails(self):
        print(" Enter Details")
        self.admin=input("Enter Admin Name:")
        self.doctor = input("Enter Doctor Name:")
        self.sister = input("Enter Sister Name:")
        self.department = input("Enter  Department:")
class department(hospital):
    def display(self):
        print("Enter Details Are")
        print("Admin name:{} Doctor Name:{} Sister Name:{} Department:{}".format(self.admin, self.doctor, self.sister, self.department))

class  patientward(department):
    def __init__(self,name,age,disease):
        self.name=name
        self.age=age
        self.disease=disease
    def getpatientdetails(self):
        self.name=input("Enter the Patient Name:")
        self.name =int(input("Enter Patient Age:"))
        self.disease = input("Enter Patient Disease:")
    def putpatientdetails(self):
        print("Patient Details:")
        print("Patient Name:{} Patient Age:{} Patient Disease:{}".format(self.name, self.age, self.disease))


obj=patientward('','','')
obj.getpatientdetails()
obj.putpatientdetails()
obj.getdetails()
obj.display()
