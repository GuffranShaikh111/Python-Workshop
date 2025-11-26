class Aadhar:
    def __init__(self, name,aadhar_number,dob,finger_print,retina):
        self.name = name
        self.aadhar_number = aadhar_number
        self.dob = dob
        self.finger_print = finger_print
        self.retina = retina

    def display_userData(self):
        print(f"{self.name,self.aadhar_number,self.dob,self.finger_print,self.retina}")
    def getRetina(self):
        return self.retina

var=Aadhar("Guffran","48916960","15/10/2003","adcabc","ghfghg")
var.display_userData()
var.getRetina()
retina_var=var.getRetina()
print(retina_var)