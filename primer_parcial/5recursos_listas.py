""" 
===============================
Si es la primera vez que abrís uno de estos archivos te recomiendo mirar el readme.
===============================
 """

# Enunciado:
""" 
Hacer una función que reciba un string y que imprima solamente los caracteres que sean vocales.
 """
# Implementación:
""" 
def mostrar_vocales(palabra): # Defino el encabezado de la función.
    res = "" # Defino un string vacío.
    vocales = ['a','á','e','é','i','í','o','ó','u','ú'] # Defino una lista de strings.
    for letra in palabra: # Defino el encabezado del ciclo. Recorriendo las letras de una palabra letra a letra.
        if letra.lower() in vocales: # Verifico si la letra está en la lista de vocales.
            res += letra # En caso afirmativo agrego la letra al string vacío que definí antes.
    return res # Devuelvo el string con todas las vocales de la palabra pasada por parámetro.
 """
# Enunciado:
""" 
Hacer una función que reciba un string y que lo invierta.
 """
# Implementación:
""" 
def invertir_palabra(palabra): # Defino el encabezado de la función.
    res = "" # Defino un string vacío.
    for i in range(len(palabra)-1,-1,-1): # Defino el encabezado del ciclo. Estableciendo una sucesión de números desde la longitud de la palabra menos uno hasta cero.
        res += palabra[i] # Agrego al string vacío la letra que está en la posición i y el ciclo vuelve a su encabezado.
    return res # Retorno el string con las letras de la palabra original, en orden invertido.
 """
# Enunciado:
""" 
Hacer una función que reciba dos strings, un string y un substring, es decir,
que el primero contiene al segundo, se pide devolver el string habiendo eliminado el substring del mismo.
 """
# Implementación:
""" 
def eliminar_silabas(palabra, silaba): # Defino el encabezado de la función.
    return palabra.replace(silaba, '') # Retorno la palabra ingresada sin la silaba pasada por parámetro.
 """
# Enunciado:
""" 
Un chef está armando una lista de supermercado con todos los ingredientes que hay que comprar.
Sólo quiere agregar un ingrediente a la lista si no lo escribió antes, así no tiene repetidos.
Hacer un programa que inserte un nuevo elemento en una lista de strings, solamente si el elemento
que se desea insertar no se encuentra en la lista.
 """
# Implementación:
""" 
def lista_de_compras(): # Defino el encabezado de la función.
    res = [] # Defino una lista vacía.
    ingrediente = input("Ingrese un producto. 'X' para terminar: ") # Le pido al usuario que me ingrese un ingrediente.
    while ingrediente != 'X': # Defino el encabezado del ciclo. Estableciendo que su cuerpo se repita mientras ingrediente sea distinto de 'X'.
        if ingrediente not in res: # Verifico si el ingrediente no está en la lista vacía que definí anteriormente.
            res.append(ingrediente) # En ese caso agrego el ingrediente a la lista.
        ingrediente = input("Ingrese un producto. 'X' para terminar: ") # Le vuelvo a pedir al usuario que me ingrese un ingrediente.
    return res # Retorno la lista con los ingredientes, sin repeticiones.
 """
# Enunciado:
""" 
Agustina está jugando a las cartas con sus amigos. A ella le gusta tener las cartas de su mano bien ordenadas.
Esto significa que cada vez que tiene que agarrar una nueva carta, la quiere agregar a su mano en el lugar indicado
para no romper el orden. Si se tiene una lista de enteros ordenadas de mayor a menor. Hacer una función que según
esta lista inserte un nuevo entero, manteniendo el orden. ¿En este caso nos conviene usar append?
 """
# Implementación:
""" 
def ordenar_mano(mano): # Defino el encabezado de la función.
    carta = int(input("¿Que carta agarro? Si no agarró, ingrese 0 ")) # Le pido al usuario que me ingrese una carta.
    while carta > 0: # Defino el encabezado del ciclo. Estableciendo que su cuerpo se repita hasta que carta sea menor a cero.
        if len(mano) == 0: # Verifico si hay alguna carta en la mano ingresada, una lista.
            mano.append(carta) # En ese caso la agrego al final de la mano.
        else: # En caso contrario.
            encontrada = False # Defino una variable con el valor falso.
            for i in range(len(mano)): # Defino el encabezado del ciclo. Estableciendo una sucesión de números desde cero hasta la longitud de la lista ingresada por parámetro menos uno.
                if carta >= mano[i]: # Verifico si la carta ingresada anteriormente es mayor o igual a la carta que esta en la posición i.
                    # En ese caso agrego la carta en esa posición e invierto el valor de verdad de la variable definida anteriormente y corto el ciclo for.
                    mano.insert(i, carta)
                    encontrada = True
                    break
            if not encontrada: # Verifico si la carta es la mas chica de la mano.
                mano.append(carta) # La agrego al final.
        carta = int(input("¿Que carta agarro? Si no agarró, ingrese 0 ")) # Le vuelvo a pedir al usuario que me ingrese una carta.
    return mano # Devuelvo la mano ordenada.
 """
# Enunciado:
""" 
Santiago armó una lista con el pedido de empanadas de su familia pero
ahora quiere saber la cantidad de gustos diferentes que tiene que pedir.
 """
# Implementación:
""" 
def gustos_de_empanada(pedido): # Defino el encabezado de la función.
    res = [] # Defino una lista vacía.
    for gusto in pedido: # Defino el encabezado del ciclo. Recorriendo el pedido, una lista, gusto por gusto.
        if gusto not in res: # Verifico si el gusto no está en la lista que definí anteriormente.
            res.append(gusto) # En ese caso la agrego.
    return len(res) # Devuelvo la cantidad de elementos que tiene la lista que defini, sin gustos repetidos.
 """
# Enunciado:
""" 
Hacer una función que reciba una lista de enteros, y devuelva otra lista que
solamente contenga los números pares, que vienen a ser las tareas de Manuel.
 """
# Implementación:
""" 
def tareas_manuel(tareas): # Defino el encabezado de la función.
    res = [] # Defino una lista vacía.
    for tarea in tareas: # Defino el encabezado del ciclo. Recorriendo las tareas, una lista, tarea a tarea.
        if tarea % 2 == 0: # Verifico si la tarea es par
            res.append(tarea) # En ese caso la agrego a la lista que definí anteriormente.
    return res # Retorno las lista con las tareas pares.
 """
# Contexto:
# Un matrimonio está organizando una fiesta y tiene que armar una lista de invitados.
# Cada uno tiene su propia tupla y guarda en ella a todos los que quiere invitar.
# Enunciado:
""" 
Si alguien cancela tienen que sacarlo de la tupla. Hacer una función que reciba la
tupla y un nombre , y devuelva una nueva tupla sin el nombre pasado por parámetro.
 """
# Implementación
""" 
def eliminar_invitado(invitados, invitado_cancelado):
    res = [] # Defino una lista vacía
    for invitado in invitados: # Defino el encabezado del ciclo. Recorriendo los invitados, una tupla, invitado a invitado.
        if invitado != invitado_cancelado: # Verifico si el invitado no es el que cancelo.
            res.append(invitado) # En ese caso lo agrego a la lista que definí anteriormente.
    return tuple(res) # Retorno la tupla de los invitados sin el que cancelo.
 """
# Enunciado:
""" 
Cuando ya tienen a todos los invitados tienen que juntar sus tuplas.
Hacer una función que a partir de dos tuplas cree una sola que sea la combinación de ambas tuplas.
 """
# Implementación:
""" 
def juntar_tuplas(tupla1, tupla2): # Defino el encabezado de la función.
    return tupla1 + tupla2 # Retorno la concatenación de las dos tuplas pasadas por parámetro.
 """