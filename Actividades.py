# 2 Ejemplo con f_strings
nombre = "Juan"
edad = 25

print(f"hola,mi nombre es {nombre} y tengo {edad} años.")

numero1 = 10

print(f"el doble del numero {numero1} es {numero1*2}.")

#3 programa basico

frutas = ["manzana", "pera", "uva"]
precios = (2000, 1500, 1800)  
inventario = {"manzana": 10, "pera": 8, "uva": 15}

usuario = "admin"

intentos = 0
while intentos < 3:
    entrada = input("Escribe el usuario: ")
    if entrada == usuario:
        print(f"Bienvenido {entrada}. Tenemos {inventario} en la seccion de fruta.")
        break
    else:
        print("Usuario incorrecto, intenta de nuevo mas tarde.")
        intentos += 1
        
        
        
        
#ejemplo sencillo

class Persona:
    def __init__(self, nombre, edad):   # Constructor con atributos
        self.nombre = nombre
        self.edad = edad

    def saludar(self):   # Método
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

p1 = Persona("Lucía", 21)
p1.saludar()
