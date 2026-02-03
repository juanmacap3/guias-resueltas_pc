""" 
===============================
Si es la primera vez que abrís uno de estos archivos te recomiendo mirar el readme.
===============================
 """

# Enunciado
""" 
Crear una lista con los números del 1 al 10. Acceder con el índice a la posición que contiene el número 5, e imprimirlo por pantalla.
Recordar que el índice de las listas empiezan con 0.
 """
# Implementación:
""" 
lista = [1,2,3,4,5,6,7,8,9,10] # Defino una lista.
print(lista[4]) # Muestro el valor número 5 accediendo por su índice en la lista.
 """
# Enunciado
""" 
Con la lista del punto anterior, usar la función len() para averiguar su longitud, e imprimirla.
 """
# Implementación:
""" 
lista = [1,2,3,4,5,6,7,8,9,10] # Defino una lista.
longitud_lista = len(lista) # Uso la función len() para saber la longitud de la lista.
print(longitud_lista) # Muestro la longitud de la lista.
 """
# Enunciado:
""" 
Crear una secuencia con números distintos, y luego devolver el elemento máximo y el mínimo.
 """
# Implementación:
""" 
numeros = [3,2,5,1] # Defino una lista.
def maximo(lista_de_numeros): # Defino el encabezado de la función.
    num_maximo = lista_de_numeros[0] # Defino una variable como el primer valor de la lista.
    for numero in lista_de_numeros: # Defino el encabezado del ciclo. Recorriendo la lista valor a valor.
        if num_maximo < numero: # Verifico que el número en el que me encuentro sea mayor que la variable que definí anteriormente.
            num_maximo = numero # En caso afirmativo sobreescribo la variable que definí anteriormente por el número actual.
    return num_maximo # Retorno el valor.

def minimo(lista_de_numeros): # Defino el encabezado de la función.
    num_minimo = lista_de_numeros[0] # Defino una variable como el primer valor de la lista.
    for numero in lista_de_numeros: # Defino el encabezado del ciclo. Recorriendo la lista valor a valor.
        if num_minimo > numero: # Verifico que el número en el que me encuentro sea mayor que la variable que definí anteriormente.
            num_minimo = numero # En caso afirmativo sobreescribo la variable que definí anteriormente por el número actual.
    return num_minimo # Retorno el valor.
 """
# Aclaración:
""" 
También puede hacerse así: max(numeros); min(numeros)
 """
# Enunciado:
""" 
Ordenar la secuencia del ejercicio anterior, e imprimirla por pantalla.
 """
# Implementación:
""" 
def ordenar_secuencia(lista_de_numeros): # Defino el encabezado de la función.
    res = [] # Defino una variable con una lista vacía.
    i = 0 # Defino una variable de control.
    while len(lista_de_numeros) > 0: # Defino el encabezado del ciclo. Estableciendo que se repita su cuerpo mientras la longitud de la lista ingresada por parámetro sea mayor a cero.
        if lista_de_numeros[i] == minimo(lista_de_numeros): # Verifico que el elemento que esta la posición de la variable de control sea igual al valor minimo de la lista, usando la función minimo del ejercicio anterior.
            # En caso afirmativo agrego el elemento a la lista que definí como vacía (1), elimino el elemento de la lista (2), y defino a la variable de control con el valor de cero (3).
            res.append(lista_de_numeros[i]) # (1)
            lista_de_numeros.pop(i) # (2)
            i = 0 # (3)
        else : i+=1 # En cualquier caso incremento el valor de la variable de control.
    return res # Retorno la lista ordenada de menor a mayor.
 """
# Aclaración:
""" 
1. Se puede realizar con sort() o sorted() también
2. Al no decir cual es el criterio de orden, decidí ordenarla de menor a mayor, en caso de ordenarla en el otro sentido únicamente hay que cambiar la función minimo por maximo.
 """
# Enunciado:
""" 
Crear una tupla que guarde tu nombre y tu edad. Luego, imprimir por pantalla tu edad,
accediendo al elemento de la tupla que corresponda.
 """
# Implementación:
""" 
informacion = ("Juan", 21)
print(informacion[1])
 """
# Enunciado: 
""" 
Hacer una lista con 5 nombres, y realizar las siguientes actividades con la misma:
    a. Cambiar el último elemento de la lista y cambiar el último nombre por "Juan". ¿Cómo podría
    saber cuál es el último elemento si no sé la longitud?
    b. Devolver el nombre que esté a dos posiciones del final.
    c. Recorrer la lista e imprimir cada nombre por pantalla.
    d. Imprimir por pantalla la lista con 3 repeticiones, usar el operador repetición (*).
 """
# Implementación:
"""
# Implementación A:
nombres = ["Schor", "Baldassarra", "Ronaldo", "Vazquez", "Salomon"] # Defino una lista de strings.
nombres[-1] = "Juan" # Agrego en la última posición el nombre "Juan".
# Implementación B:
print(nombres[-3]) # Muestro el nombre que esta en la posición antepenúltima.
# Implementación C:
for nombre in nombres: # Defino el encabezado del ciclo. Recorriendo la lista nombre a nombre.
    print(nombre) # Muestro un nombre y el ciclo vuelve a su encabezado.
# Implementación D:
print(nombres*3) # Muestro tres veces seguidas la lista.
"""
# Enunciado:
""" 
Se pide ahora crear 3 tuplas como las del ejercicio 5, con un nombre y una edad.
A continuación, guardarlas en una lista.
 """
# Implementación: 
""" 
lista_informacion = [("Schor", 25), ("Baldassarra", 26), ("Ronaldo", 29)] # Defino una lista de tuplas.
 """
# Enunciado:
""" 
Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.
    a. Crear una tupla para cada país que contenga su nombre, su capital y el continente donde se encuentra.
    b. Guardar las tuplas en una lista.
    c. Hacer una función que reciba por parámetros la lista, e imprima la información de cada país con el siguiente formato:
        País: <nombre>
        Capital: <capital>
        Continente: <continente>
 """
# Implementación inciso A:
""" 
informacion_arg = ("Argentina", "CABA", "América del sur") # Defino una tupla de strings.
informacion_peru = ("Perú", "Lima", "América del sur") # Defino una tupla de strings.
informacion_francia = ("Francia", "Paris", "Europa") # Defino una tupla de strings.
informacion_japon = ("Japón", "Tokyo", "Asia") # Defino una tupla de strings.
informacion_alemania = ("Alemania", "Berlin", "Europa") # Defino una tupla de strings.
 """
# Implementación inciso B:
""" 
lista_paises = [informacion_arg, informacion_peru, informacion_francia, informacion_japon, informacion_alemania] # Defino una lista de tuplas.
 """
# Implementacion inciso C:
""" 
def mostrar_informacion_pais(paises): # Defino el encabezado.
    for pais in paises: # Defino el encabezado del ciclo. Recorriendo la lista país a país.
        # De cada país, tupla, muestro los datos que almacena.
        print("País: " + pais[0])
        print("Capital: " + pais[1])
        print("Continente: " + pais[2])
 """
# Enunciado:
""" 
Una librería tiene un sistema que guarda los nombres de todos los libros que tienen
en una lista de la siguiente forma: ["El principito", "It", "Sherlock Holmes"...].
Se quiere saber cuántos libros repetidos tienen. Hacer código que imprima para cada título, cuántos ejemplares hay.
 """
# Implementación:
""" 
def contar_apariciones_libros(libros, titulo): # Defino el encabezado de una función auxiliar.
    res = 0 # Defino una variable con el valor cero.
    for libro in libros: # Defino el encabezado del ciclo. Recorriendo la lista libro a libro.
        if libro == titulo: # Verifico si el libro es igual al titulo pasado por parámetro.
            res += 1 # En caso afirmativo incremento la variable definida anteriormente.
    return res # Retorno la cantidad de veces que aparece el titulo en la lista libros.

def mostrar_stock_libros(libros): # Defino el encabezado de la función.
    libros_mostrados = [] # Defino una lista vacía.
    for libro in libros: # Defino el encabezado del ciclo. Recorriendo la lista libro a libro.
        if libro not in libros_mostrados: # Verifico si un elemento no esta en la lista que definí anteriormente.
            print(f"La cantidad de ejemplares de {libro} es {contar_apariciones_libros(libros, libro)}") # Muestro la cantidad de ejemplares del libro, usando la función auxiliar contar_apariciones_libros.
            libros_mostrados.append(libro) # Agrega el libro en la lista que definí anteriormente y el ciclo vuelve a su encabezado.
 """
# Enunciado
""" 
Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos
números elevados al cuadrado.
 """
# Implementación:
""" 
def elevar_al_cuadrado(lista): # Defino el encabezado de la función.
    res = [] # Defino una lista vacía.
    for numero in lista: # Defino el encabezado del ciclo. Recorriendo la lista número a número.
        res.append(numero**2) # Agrego, a la lista que definí anteriormente, cada uno de los números de la lista original elevados al cuadrado.
    return res # Retorno la lista con los elementos de la lista original elevados al cuadrado.
 """
# Enunciado:
""" 
Se tiene la siguiente lista de palabras: ["entender", "pueden", "humanos", "los", "que", "código",
"escriben", "programadores", "buenos", "Los", "entiende.", "computadora", "una", "que", "código",
"escribe", "tonto", "Cualquier"].
Hacer una función que reciba una lista, y devuelva un string uniendo las palabras desde el final
de la lista hasta el principio con un " " (espacio) entre cada una, para formar la frase.
 """
# Implementación:
""" 
oracion = ["entender", "pueden", "humanos", "los", "que", "código", "escriben", "programadores", "buenos", "Los", "entiende.", "computadora", "una", "que", "código", "escribe", "tonto", "Cualquier"] # Defino una lista de strings.
def formar_palabra(palabras): # Defino el encabezado de la función.
    res = "" # Defino un string vacío.
    for i in range(len(palabras)-1, -1, -1): # Defino el encabezado del ciclo. Estableciendo una sucesión de números desde el la longitud de la palabra menos uno hasta el 1.
        res += palabras[i] # Agrego una palabra
        if i != 0: # Verifico si la palabra no es la última.
            res += " " # En ese caso agrego un espacio en blanco.
    res += '.' # Al final le agrego un punto a la palabra.
    return res # Retorno el string con la palabra.
 """
# Enunciado:
""" 
Se quiere hacer un sistema en la facultad para que un alumno pueda ir guardando las materias que va haciendo.
Para eso, crear una función que le pregunte al usuario la materia que quiere almacenar, e ir guardando la
información en una lista hasta que ingrese una ‘X’.
 """
# Implementación:
""" 
def guardar_materias(): # Defino el encabezado de la función.
    materia = input("Ingrese la materia que quiera guardar. Si no quiere guardar más materias, ingrese 'X': ") # Le pido al usuario una materia.
    res = [] # Defino una lista vacía.
    while materia != 'X': # Defino el encabezado del ciclo. Estableciendo que su cuerpo se recorra hasta que materia sea igual a 'X'.
        res.append(materia) # Agrego a la lista vacía, definida anteriormente, la materia.
        materia = input("Ingrese la materia que quiera guardar. Si no quiere guardar más materias, ingrese 'X': ") # Le vuelvo a pedir al usuario una materia.
    return res # Retorno la lista con las materias.
 """
# Enunciado:
""" 
Se tiene un ticket de supermercado que se puede representar como una lista de tuplas (producto, precio).
    a. Hacer una función que reciba la lista y calcule y devuelva el total que hay que pagar.
    b. Ahora se tienen dos tickets. Juntar ambos y volver a calcular el total.
 """
# Implementación A:
""" 
ticket_compra = [("yerba", 242), ("harina", 4244), ("Salsa", 934), ("Aceite", 2412)] # Defino una lista de tuplas.
def monto_total(ticket): # Defino el encabezado de la función.
    res = 0 # Defino una función con el valor 0.
    for producto in ticket: # Defino el encabezado del ciclo. Recorriendo la lista producto a producto.
        res += producto[1] # Sumo el precio de cada producto y el ciclo vuelve a su encabezado.
    return res # Retorno la sumatoria de todos los precios.
 """
# Implementación B:
""" 
ticket_compra2 = [("Queso", 8342), ("Cafe", 542), ("Cebolla", 183), ("Galletitas", 532)] # Defino una lista de tuplas.
ticket_compra += ticket_compra2 # Concateno las dos listas de tuplas.
print(monto_total(ticket_compra)) # Muestro la sumatoria de los precios de los productos de ambos tickets.
 """
