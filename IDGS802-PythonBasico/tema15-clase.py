
import os

class OperasBas:
    # declaracion de propiedades de la clase
    num1 = 0
    num2 = 0
    res = 0

    # declaracion del constructor

    def __init__(self, a,b):
        self.num1 = a
        self.num2 = b

    # declaracion de metodos de clase

    def suma(self):
       # num1 = 12
       # num2 = 10
        self.res = int(self.num1) + int(self.num2)
        print("La suma es: {}".format(self.res))

    def resta(self):
        self.res = int(self.num1) - int(self.num2)
        print("La resta es: {}".format(self.res))

    def mult(self):
        self.res = int(self.num1) * int(self.num2)
        print("La multiplicacion es: {}".format(self.res))
    
    def div(self):
        self.res = int(self.num1) / int(self.num2)
        print("La divicion es: {}".format(self.res))
        

def main():
    os.system('cls')
    respuesta = input("1. suma, 2. resta, 3. multiplicacion, 4, divicion, 5 salir: ")
    
    while int(respuesta) != 5:
        os.system('cls')
        if int(respuesta) == 1 :
            obj = OperasBas(int(input("num1: ")),input(("num2: ")))
            obj.suma()
        
        if int(respuesta) == 2 :
            obj = OperasBas(int(input("num1: ")),input(("num2: ")))
            obj.resta()
           
        if int(respuesta) == 3 :
            obj = OperasBas(int(input("num1: ")),input(("num2: ")))
            obj.mult()
        
        if int(respuesta) == 4 :  
            obj = OperasBas(int(input("num1: ")),input(("num2: ")))
            obj.div()
            
        respuesta = input("1. suma, 2. resta, 3. multiplicacion, 4, divicion, 5 salir: ")

if __name__ == "__main__":
    main()




