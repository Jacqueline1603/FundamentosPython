class Alumno:
    name = ''
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def lista(self):
        print(f"{ self.name } Presente!")
    
alumno1 = Alumno('Jose', 20)
alumno1.lista()
alumno2 = Alumno('Pedro', 20)
alumno2.lista()
alumno3 = Alumno('Mike', 18)
alumno3.lista()
