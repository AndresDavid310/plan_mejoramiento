# 2 Ejemplo con f_strings
nombre = "Juan"
edad = 25

print(f"hola,mi nombre es {nombre} y tengo {edad} años.")

numero1 = 10

print(f"el doble del numero {numero1} es {numero1*2}.")

#3 programa basico

# Listas, tuplas, diccionarios y cadenas
frutas = ["manzana", "pera", "uva"]
precios = (2000, 1500, 1800)  
inventario = {"manzana": 10, "pera": 8, "uva": 15}

usuario = "admin"

# Bucle while con condicionales
intentos = 0
while intentos < 3:
    entrada = input("Escribe el usuario: ")
    if entrada == usuario:
        print(f"Bienvenido {entrada}. Tenemos {inventario} en stock.")
        break
    else:
        print("Usuario incorrecto, intenta de nuevo.")
        intentos += 1
