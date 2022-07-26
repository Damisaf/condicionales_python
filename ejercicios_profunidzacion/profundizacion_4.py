# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA:
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
palabra_1 = input("ingrese palabra 1: ")
palabra_2 = input("ingrese palabra 2: ")
palabra_3 = input("ingrese palabra 3: ")
orden = input("ingrese [1]-alfabetico [2]-por longitud: ")


if orden == "1":
    if palabra_1 > palabra_2 and palabra_1 > palabra_3:
        ordenadas = palabra_1
        if palabra_2 > palabra_3:
            ordenadas = ordenadas + " " + palabra_2 + " " + palabra_3
        else:
            ordenadas = ordenadas + " " + palabra_3 + " " + palabra_2
    elif palabra_2 > palabra_1 and palabra_2 > palabra_3:
        ordenadas = palabra_2
        if palabra_1 > palabra_3:
            ordenadas = ordenadas + " " + palabra_1 + " " + palabra_3
        else:
            ordenadas = ordenadas + " " + palabra_3 + " " + palabra_1
    else:
        ordenadas = palabra_3
        if palabra_1 > palabra_2:
            ordenadas = ordenadas + " " + palabra_1 + " " + palabra_2
        else:
            ordenadas = ordenadas + " " + palabra_2 + " " + palabra_1

print(ordenadas)

