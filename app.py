from flask import Flask


class Miro:
    def __init__(self, name, age):
        self.name=name
        self.my_year=age
        
    def my_Name(self):
        return self.name   

    def my_age(self):
        return self.my_year

f = Miro("hero", 30)   #f is an object
print(f.my_age())  
z = Miro("zero", 40)
print(z.my_Name())   



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('DEBUG') == 'True')


            
