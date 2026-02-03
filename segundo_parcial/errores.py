""" 
===============================
Si es la primera vez que abrís uno de estos archivos te recomiendo mirar el readme.
===============================
 """

# Enunciado
""" 
1. Se quiere hacer un programa para pedirle al usuario que ingrese un número entero, y en caso de que el
valor ingresado no sea un número entero, mostrarle un mensaje apropiado.
    a. Realizarlo utilizando isnumeric(). ¿Qué limitaciones encuentra?
    b. Realizarlo utilizando try/ except.
 """
# Respuesta inciso a
""" 
Las limitaciones que tiene es que isnumeric() devuelve falso cuando ingresamos un número negativo, decimal o con espacios.
 """
# Implementación inciso a
""" 
num = input("Ingrese un número entero: ") # Le pido al usuario un número entero.
while not num.isnumeric(): # Defino el encabezado del ciclo. Repitiendo su código hasta que el número ingresado sea efectivamente un número.
    # En el caso de que no haya ingresado un número se muestra por pantalla un mensaje de error y se le vuelve a pedir un número entero.
    print("Error, ingreso un dato que no es un número entero.")
    num = input("Ingrese un número entero: ")
 """
# Implementación inciso b.
""" 
try: # Intento pedirle un número al usuario.
    num = int(input("Ingrese un número entero: "))
except: # En el caso de que salte alguna excepción muestro un mensaje.
    print("Error, ingreso un dato que no es un número entero.")
 """
# Enunciado
""" 
Crear una función, utilizando el punto anterior, que le pida al usuario un número entero. Utilizarla para
calcular el producto entre dos números enteros ingresados.
 """
# Implementación
# Aclaración
""" 
Voy a usar la versión del inciso a porque me parece mas robusta y voy a devolver el producto, aunque no lo aclare.
 """
""" 
def calcular_producto(): # Defino el encabezado de la función
    # Le pido al usuario dos números.
    num1 = input("Ingrese un primer número entero: ")
    num2 = input("Ingrese un segundo número entero: ")
    while not (num1.isnumeric() and num2.isnumeric()): # Defino el encabezado del ciclo. Repitiendo su código hasta que ambos datos sean números.
        print("Alguno de los dos datos ingresados no es un número entero.") # En caso de que alguno no lo sea muestro este mensaje.
        if not num1.isnumeric(): # Verifico si el primer dato no es un número.
            num1 = input("Ingrese un primer número entero: ") # En ese caso solo vuelvo a pedir el primer número.
        elif not num2.isnumeric(): # Verifico si el segundo dato no es un número.
            num2 = input("Ingrese un segundo número entero: ") # En ese caso solo vuelvo a pedir el segundo número.
    producto = int(num1) * int(num2) # Calculo el producto.
    return producto # Devuelvo el producto entre ambos números.
 """
# Enunciado
""" 
Se quiere hacer un programa que le solicite al usuario un número divisor y un dividendo, y calcule el
cociente entre ellos.
AYUDA: Considerar que el usuario podría brindar un valor no numérico o un divisor nulo.
 """
# Implementación
""" 
variable_control = True

while variable_control: # Defino el encabezado del ciclo. Se repite el cuerpo mientras que variable_control tenga el valor de verdad verdadero.
    try: # Intento pedirle al usuario dos números, calcular una división y modificar el valor de verdad de la variable de control.
        dividendo = int(input("Ingrese el dividendo de una división: ")) # Le pido el dividendo.
        divisor = int(input("Ingrese el divisor de una división: ")) # Le pido el divisor.
        resultado = dividendo / divisor # Calculo la división.
        variable_control = False # Modifico el valor de verdad de la variable de control.
    except ValueError: # En el caso de que se produzca una excepción del tipo ValueError.
        print("Ambos valores deben ser números enteros.") # Muestro un mensaje.
    except ZeroDivisionError: # En el caso de que se produzca una excepción del tipo ZeroDivisionError.
        print("No se puede dividir por cero.") # Muestro otro mensaje.
 """
# Enunciado
""" 
Crear un programa para abrir un archivo llamado “file.txt” en modo lectura y en caso de que este
archivo no exista, mostrar el mensaje “No se pudo encontrar el archivo file.txt”.
 """
# Implementación
""" 
try: # Intento abrir en modo lectura un archivo y cerrarlo.
    archivo = open("file.txt", "r")
    archivo.close()
except: # En el caso de que salte alguna excepción muestro un mensaje.
    print("No se pudo encontrar el archivo file.txt.")
 """
# Enunciado
""" 
Crear una función cuyos parámetros sean una lista y un índice de posición para mostrar el valor de la
lista en esa ubicación.
    a. ¿Qué ocurre si ingreso un índice que se encuentra fuera del rango?
    b. Si el valor del índice ingresado se encuentra dentro del rango, mostrar el valor. En caso
        contrario, mostrar un mensaje apropiado para dicho error.
 """
# Implementación inciso a.
""" 
def mostrar_valor(lista, indice): # Defino el encabezado de la función
    print(lista[indice]) # Muestro el valor que está almacenado en el índice de la lista.
 """
# Aclaración
""" 
Con esta implementación, si ingresamos un índice fuera del rango vamos a obtener una excepción.
 """
# Implementación inciso b.
""" 
def mostrar_valor(lista, indice): # Defino el encabezado de la función
    try: # Intento mostrar el valor que está almacenado en el índice de la lista.
        print(lista[indice])
    except: # En el caso de que salte alguna excepción muestro un mensaje.
        print("El índice está fuera del rango.")
 """
# Enunciado
""" 
Para jugar al chinchón con un único mazo de cartas españolas, el número de jugadores puede ser: dos,
tres o cuatro. Crear una función que pida al usuario informar el número de jugadores, considerando
que este puede ingresar:
    ● un valor no válido, por ejemplo, una palabra.
    ● un valor menor a 2, en en cuyo caso, mostrar el mensaje "Debe haber al menos 2 jugadores."
    ● un valor mayor a 4, en cuyo caso, mostrar el mensaje "Se puede jugar con un máximo de 4
    jugadores."
    ● un valor válido, en cuyo caso, mostrarlo.
 """
# Implementación
""" 
def jugar_chinchon(): # Defino el encabezado de la función.
    try: # Intento pedirle al usuario la cantidad de jugadores.
        cant_jugadores = int(input("Ingrese la cantidad de jugadores: "))
    except: # Si salta alguna excepción muestro un mensaje por pantalla.
        print("El valor ingresado no es válido.")
    else: # En caso de que el dato ingresado haya sido un número.
        if cant_jugadores < 2: # Verifico si es menor a dos.
            print("Debe haber al menos 2 jugadores") # En este caso muestro un mensaje por pantalla.
        elif cant_jugadores > 4: # Verifico si es mayor a cuatro.
            print("Se puede jugar con un máximo de 4 jugadores") # En este caso muestro otro mensaje por pantalla.
        else: # En cualquier otro caso muestro la cantidad de jugadores.
            print("La cantidad de jugadores es: ",cant_jugadores) 
 """
# Enunciado
""" 
Para jugar al truco con un único mazo de cartas españolas, el número de jugadores puede ser: dos,
cuatro o seis. Crear una función que pida al usuario informar el número de jugadores, considerando
que este puede ingresar:
    ● un valor no válido, por ejemplo, una palabra.
    ● un valor menor a 2, en en cuyo caso, mostrar el mensaje "Debe haber al menos 2 jugadores."
    ● un valor mayor a 6, en cuyo caso, mostrar el mensaje "Se puede jugar con un máximo de 6
    jugadores.".
    ● un valor impar, como 3 y 5, en cuyo caso, mostrar el mensaje "Debe haber un número par de
    jugadores.".
    ● un valor válido, en cuyo caso, mostrarlo.
 """
# Implementación
""" 
def jugar_truco(): # Defino el encabezado de la función.
    try: # Intento pedirle al usuario la cantidad de jugadores.
        cant_jugadores = int(input("Ingrese la cantidad de jugadores: "))
    except: # Si salta alguna excepción muestro un mensaje por pantalla.
        print("El valor ingresado no es válido.")
    else: # En caso de que el dato ingresado haya sido un número.
        if (cant_jugadores < 2): # Verifico si es menor a dos.
            print("Debe haber al menos 2 jugadores") # En este caso muestro un mensaje por pantalla.
        elif (cant_jugadores > 6): # Verifico si es mayor a seis.
            print("Se puede jugar con un máximo de 6 jugadores.") # En este caso muestro otro mensaje por pantalla.
        elif (cant_jugadores >= 2 and cant_jugadores <= 6) and (cant_jugadores % 2 != 0): # Verifico si la cantidad de jugadores está entre dos y seis pero si es impar.
            print("Debe haber un número par de jugadores.") # En este caso muestro otro mensaje por pantalla.
        else: # En cualquier otro caso muestro la cantidad de jugadores.
            print("La cantidad de jugadores es: ",cant_jugadores)
 """
# Enunciado
""" 
El kiosko de la facultad quiere automatizar un letrero que tome datos de un programa y le cobre al
estudiante.
Se tienen dos diccionarios, uno con un código y el producto, y otro con el código y el precio de cada
producto.
Ejemplo:
opciones = {
1: "hamburguesas",
2: "milanesas",
3: "gaseosa",
4: "alfajor",
5: "papas fritas",
6: "agua"
}
valores = {
1:1000,
2:1500,
3:500,
4:300,
5:600,
6:350
}
Se quiere hacer un programa que muestre la información de la siguiente forma en la pantalla:
1: hamburguesas -> 1000
2: milanesas -> 1500
3: gaseosa -> 500
4: alfajor -> 300
5: papas fritas -> 600
6: agua -> 350
Y le pida al usuario una opción y una cantidad. Luego, debe imprimir el total a pagar.
Se debe considerar que el usuario podría ingresar una opción que no está en el diccionario, o ingresar
una opción que no sea un número. El usuario debe en esos casos imprimir un mensaje de error que sea
descriptivo y volver a pedirle al usuario que ingrese una opción.
 """
# Implementación
""" 
# Defino los diccionarios
opciones = {
1: "hamburguesas",
2: "milanesas",
3: "gaseosa",
4: "alfajor",
5: "papas fritas",
6: "agua"
}
valores = {
1:1000,
2:1500,
3:500,
4:300,
5:600,
6:350
}
variable_de_control = True
while variable_de_control: # Defino el encabezado del ciclo. Se repite el cuerpo mientras que variable_de_control tenga el valor de verdad verdadero.
    try: # Intento pedirle al usuario dos números.
        opc_ingresada = int(input("Ingrese la opción que quiera comprar: ")) # Le pido al usuario una opción
        cantidad_ingresada = int(input("Ingrese la cantidad que quiera consumir: ")) # Le pido una cantidad para dicho producto.
    except ValueError: # En caso de tener la excepción ValueError.
        print("En ambas opciones debe ingresar un número.") # Muestro este mensaje.
    else: # En caso de que no haya saltado la excepción.
        if opc_ingresada not in opciones: # Verifico si la opción ingresada no está entre uno y seis.
            print("La opción debe estar entre 1 y 6.") # En ese caso muestro un mensaje.
        elif cantidad_ingresada <= 0: # Verifico si la cantidad es menor a uno.
            print("La cantidad debe ser positiva.") # En ese caso muestro otro mensaje.
        else: # En cualquier otro caso.
            total = valores[opc_ingresada] * cantidad_ingresada # Calculo cuanto debe pagar
            print("El total a pagar es: $",total) # Lo muestro por pantalla.
            variable_de_control = False # Modifico el valor de verdad de la variable de control para que termine el ciclo.
 """
