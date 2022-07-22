# 0001 Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!
# ////////////////////////////////////////////////////////////////////////////

print("Hola mundo")

# 0002 asignar un valor a una variable e imprimir esa variable
# ////////////////////////////////////////////////////////////////////////////

saludo = "Hola mundo"
print (saludo)

# 0003 ////////////////////////////////////////////////////////////////////////////

"""
Escribir un programa que pregunte el nombre del usuario en la consola y
# después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
donde <nombre> es el nombre que el usuario haya introducido.
"""
pregunta = input("Su nombre por favor")
print("hola " + pregunta)

name1 = "luis"
apellido = "Acevedo"
print(f"{name1},{apellido}")

# 0004 Una variable asignada a una lista que contiene valores
#////////////////////////////////////////////////////////////////////////////

datosPersonaje = [1985, "mayo", "casado", 37, "venezolano"]
datosPersonaje[0], datosPersonaje[2], datosPersonaje[4] #---> Llamando a elementos de una lista