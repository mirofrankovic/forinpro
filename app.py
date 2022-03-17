class Miro:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def my_Name(self):
        return self.name   

    def my_age(self):
        return self.age       

f = Miro("hero", 30)   
print(f.my_age())  
z = Miro("zero", 40)
print(z.my_Name())   