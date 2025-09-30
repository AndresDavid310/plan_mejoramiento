

#listas
frutas = ["manzana", "pera", "uva"]
print(frutas[0])   # Imprime "manzana"
frutas.append("mango")  # Agregar un elemento
print(frutas)      # ["manzana", "pera", "uva", "mango"]

#tuplas
precios = (2000, 1500, 1800)
print(precios[1])   # Imprime 1500
# precios[0] = 2500  # Error, no se puede modificar

#diccionarios
inventario = {"manzana": 10, "pera": 8, "uva": 15}
print(inventario["pera"])  # Imprime 8
inventario["mango"] = 12   # Agregar nuevo par clave-valor
print(inventario)

#cadenas de caracteres
mensaje = "Hola Mundo"
print(mensaje.lower())   # "hola mundo"
print(mensaje.upper())   # "HOLA MUNDO"
print(mensaje[0:4])      # "Hola"


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
        print(f"Usuario incorrecto, intenta de nuevo mas tarde.")
        intentos += 1
        
        

