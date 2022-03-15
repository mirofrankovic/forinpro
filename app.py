class Miro:
    def __init__(self, name):
        self.name=name
        
    def my_Name(self):
        return self.name   

   

f = Miro("hero")   
print(f.my_Name())  
z = Miro("zero")
print(z.my_Name())   