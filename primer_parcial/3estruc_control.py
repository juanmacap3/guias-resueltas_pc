""" 
===============================
Si es la primera vez que abrís uno de estos archivos te recomiendo mirar el readme.
===============================
 """

# Enunciado:
""" 
Escribir la expresión para saber si un número es más grande que otro. Guardarla en una variable de tipo
bool e imprimirla por pantalla para ver su valor.
 """
# Implementación:
""" 
evalucion = 3 > 1 # Evaluo una expresión que me devuelve un valor booleano y lo guardo en una variable. 
print(evalucion) # Muestro el valor booleano por pantalla.
 """
# Enunciado:
""" 
 Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.
 """
# Implementación:
""" 
letra = 'n'
evaluacion = not((letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u')) # Evaluo una expresión que me devuelve un valor booleano y lo guardo en una variable.
print(evaluacion) # Muestro el valor booleano por pantalla.
 """
# Enunciado:
""" 
Repetir pero para la expresión que permite saber si un número es par y menor a 10.
 """
# Implementación:
""" 
numero = 10
evaluacion = (numero % 2 == 0) and (numero < 10) # Evaluo una expresión que me devuelve un valor booleano y lo guardo en una variable. 
print(evaluacion) # Muestro el valor booleano por pantalla.
 """
# Enunciado:
""" 
Crear una función que dado un número, devuelva su valor absoluto.
El valor absoluto de un número es el mismo número sin considerar el signo.
Por ejemplo, el absoluto de 2 es 2 (|2| = 2) y el absoluto de -4 es 4 (|-4|=4).
 """
# Implementación:
""" 
def calcular_valor_absoluto(numero): # Defino el encabezado de la función.
    res = numero # Defino una variable con el valor del número ingresado a la función. 
    if numero < 0: # Verifico si el número es menor que cero.
        res = -res # En caso afirmativo le cambio el signo.
    return res # Retorno el valor absoluto del número ingresado.
 """
# Enunciado
""" 
Crear el programa al que sea imposible ganarle en el juego de “Piedra, papel o tijera”.
Cada elemento va a ser representado con una letra: R para piedra, P para papel y T para tijera.
 """
# Implementación
""" 
def jugar_piedra_papel_tijera(opc_juego): # Defino el encabezado de la función.
    if opc_juego == 'R': # Verifico que la opción ingresada sea igual al caracter 'R'.
        print("Papel ¡Te gané!") # Muestro un mensaje por pantalla.
    elif opc_juego == 'P': # Verifico que la opción ingresada sea igual al caracter 'P'.
        print("Tijera ¡Te gané!") # Muestro un mensaje por pantalla.
    elif opc_juego == 'T': # Verifico que la opción ingresada sea igual al caracter 'T'.
        print("Piedra ¡Te gané!") # Muestro un mensaje por pantalla.
    else: print("¡No vale!") # Si no se ingresa 'R', 'P' o 'T' entonces el usuario selecciono una opción incorrecta.
 """
# Enunciado
""" 
Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100.
Si la suma de ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla
un mensaje con ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
 """
# Implementación:
""" 
def suma_respecto_de_cien(primer_numero, segundo_numero): # Defino el encabezado de la función.
    suma = primer_numero + segundo_numero # Sumo los números ingresados.

    if suma < 100: # Verifico si la suma es menor a 100.
        diferencia_a_cien = 100 - suma # Calculo lo que le falta a la suma para llegar a 100. 
        print("La suma no llega a cien, faltan ", diferencia_a_cien) # Muestro por pantalla la diferencia.
    elif suma > 100: # Verifico que la suma sea mayor que 100.
        print("Llega a 100") # Muestro por pantalla.
 """
""" 
Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del usuario, y no solo para 100?.
 """
# Implementación:
""" 
def suma_respecto_de_un_limite(primer_numero, segundo_numero, limite): # Defino el encabezado de la función.
    suma= primer_numero + segundo_numero # Sumo los números ingresados.

    if suma < limite: # Verifico si la suma es menor al límite.
        diferencia_a_limite = limite - suma # Calculo lo que le falta a la suma para llegar al límite. 
        print(f"La suma no llega a {limite}, faltan {diferencia_a_limite}") # Muestro por pantalla la diferencia.
    elif suma > limite: # Verifico que la suma sea mayor que el límite.
        print("Llega a ", limite) # Muestro por pantalla.
 """
# Enunciado:
""" 
Se tienen letras para representar las estaciones del año:
    V para verano
    O para otoño
    I para invierno
    P para primavera
Crear una función que dada una letra, imprima por pantalla la estación del año que representa
(es decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a
ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O, B, V e I.
 """
# Implementación:
""" 
def estacion_del_anio(letra): # Defino el encabezado de la función.
    # Verifico si la letra ingresada es alguna de las opciones correctas, en ese caso muestro la estación que representa y sino muestro el mensaje "error".
    if letra == 'V':
        print("Verano")
    elif letra == 'O':
        print("Otoño")
    elif letra == 'I':
        print("Invierno")
    elif letra == 'P':
        print("Primavera")
    else: print("Error")
 """
# Enunciado:
""" 
Se quiere hacer un programa para enseñar a unos niños a contar. Crear una función que reciba un número entero e
imprima por pantalla los números del 1 hasta ese número con la estructura de control iterativa for.
 """
# Implementación:
# Aclaración
""" 
range(desde, hasta) genera una sucesión de números en éste intervalo [desde, hasta)
Ejemplo:
range(1,5) genera la sucesión 1,2,3,4
 """
""" 
def contar_numeros(numero): # Defino el encabezado de la función.
    for i in range(1, numero + 1): # Defino el encabezado del ciclo. Estableciendo una sucesión de números desde el 1 hasta número.
        print(i) # Muestro por pantalla cada uno de los números desde el 1 hasta el número ingresado.
 """
# Aclaración
""" 
En range al número ingresado se le suma uno porque esta función, en el caso del segundo parámetro, utiliza el número anterior al definido.
 """
# Enunciado:
""" 
Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio anterior.
Ahora se necesita una funcionalidad que permita a los niños aprender las tablas.
Crear una función que reciba un número entero e imprima por pantalla la tabla de ese número del 1 al 10.
 """
# Implementación:
""" 
def calcular_tabla(numero): # Defino el encabezado de la función.
    for i in range(1, 11): # Defino el encabezado del ciclo. Estableciendo una sucesión de números desde el 1 hasta el 10.
        producto = numero * i # Cálculo una de las filas de la tabla del número ingresado.  
        print(producto) # Muestro el cálculo y el ciclo vuelve a su encabezado.
 """
# Enunciado:
""" 
Crear una función que simule un cumpleaños: que dado un entero imprima “Que los cumplas feliz” esa cantidad de veces.
 """
# Implementación:
""" 
def cantar_feliz_cumpleanios(cantidad_de_repeticiones): # Defino el encabezado de la función.
    for i in range(cantidad_de_repeticiones): # Defino el encabezado del ciclo. Estableciendo una sucesión de números desde el 0 hasta cantidad_de_repeticiones - 1.
        print("Que los cumplas feliz") # Muestro por pantalla el mensaje.
 """
# Enunciado:
""" 
En un almacén están buscando la forma de hacer los cobros más automáticamente.
Para esto, se nos pide crear una función que reciba un número entero que representa lo que hay que cobrar,
le pida al usuario ingresar un monto, y se vaya mostrando por pantalla cuánto falta para completar el pago.
Repetir este proceso hasta que la deuda sea 0 o menor.
 """
# Implementación:
""" 
def almacen_automatizado(monto_cobro): # Defino el encabezado de la función.
    monto_ingresado = int(input("Ingrese el monto que va a abonar: ")) # Le pido al usuario un número. 
    while monto_cobro - monto_ingresado >= 0: # Defino el encabezado del ciclo. Estableciendo que se repita su bloque de código hasta que la diferencia entre el cobro y el monto ingresado sea menor a cero.
        monto_cobro -= monto_ingresado # Al cobro le resto el monto ingresado.
        print("Faltan ", monto_cobro) # Muestro cuanto le falta para completar el cobro.
        monto_ingresado = int(input("Ingrese el monto que va a abonar: ")) # Le vuelvo a pedir al usuario que me ingrese un número.
    print("Completó el pago.") # Cuando completó el pago, muestro por pantalla este mensaje.
 """
# Enunciado:
""" 
Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar,
imprimiendo un mensaje por pantalla en cada caso.
 """
""" 
for numero in range(1,21): # Defino el encabezado del ciclo. Estableciendo una sucesión de números desde el 1 hasta el 20.
    if numero % 2 == 0: # Verifico que el número sea par y en cualquiera de los dos casos lo muestro con su paridad.
        print(f"El número {numero} es par")
    else: print(f"El número {numero} es impar")
 """
# Enunciado:
""" 
Se tiene una máquina de sacar juguetes que funciona cuando se ingresa una determinada cantidad de fichas,
y se quiere hacer una función que imite ese comportamiento.
    Inciso A: Hacer una función que reciba un número que represente el precio de la máquina, e imprima
    por pantalla “Ingresá x fichas para comenzar” hasta que se hayan ingresado esa cantidad de
 """
# Implementación:
""" 
def jugar_a_los_fichines_a(cantidad_de_fichas): # Defino el encabezado de la función.
    cantidad_original_de_fichas = cantidad_de_fichas # Defino una función el valor ingresado por parámetro al comienzo de la ejecución. 
    while cantidad_de_fichas > 0: # Defino el encabezado del ciclo. Estableciendo que se repita su bloque de código hasta que la cantidad de fichas sea menor que cero.
        print(f"Ingresá {cantidad_original_de_fichas} fichas para comenzar.") # Se le pide al usuario que ingrese una ficha.
        opc_ingresada = input() # En este caso el input está separado para que sea mas prolijo pero la línea 186 y 187 podrían estar juntas en una sola.
        if opc_ingresada == 'F': # Verifico que el usuario haya ingresado una ficha.
            cantidad_de_fichas -= 1 # Resto una ficha a la cantidad ingresada por parámetro.
    print("¡A jugar!") # Muestro un mensaje por pantalla.
 """
# Enunciado    
""" Inciso B: Ahora se quiere que se vaya mostrando por pantalla, cuántas fichas FALTAN ingresar para empezar a jugar """
# Implementación:
""" 
def jugar_a_los_fichines_b(cantidad_de_fichas): # Defino el encabezado de la función.
    while cantidad_de_fichas > 0: # Defino el encabezado del ciclo. Estableciendo que se repita su bloque de código hasta que la cantidad de fichas sea menor que cero.
        print(f"Ingresá {cantidad_de_fichas} fichas para comenzar.") # Se le pide al usuario que ingrese una ficha.
        opc_ingresada = input() # En este caso el input está separado para que sea mas prolijo pero la línea 196 y 197 podrían estar juntas en una sola.
        if opc_ingresada == 'F': # Verifico que el usuario haya ingresado una ficha.
            cantidad_de_fichas -= 1 # Resto una ficha a la cantidad ingresada por parámetro.
    print("¡A jugar!") # Muestro un mensaje por pantalla.
 """
# Enunciado
""" Inciso C: Agregar a la función el mensaje de error “Por favor solamente ingrese fichas reales (F)”
    cuando se recibe una letra distinta de F. """
# Implementación inciso A:
""" 
def jugar_a_los_fichines_c1(cantidad_de_fichas): # Defino el encabezado de la función.
    cantidad_original_de_fichas = cantidad_de_fichas  # Defino una función el valor ingresado por parámetro al comienzo de la ejecución. 
    while cantidad_de_fichas > 0: # Defino el encabezado del ciclo. Estableciendo que se repita su bloque de código hasta que la cantidad de fichas sea menor que cero.
        print(f"Ingresá {cantidad_original_de_fichas} fichas para comenzar.") # Se le pide al usuario que ingrese una ficha.
        opc_ingresada = input() # En este caso el input está separado para que sea mas prolijo pero la línea 208 y 209 podrían estar juntas en una sola.
        if opc_ingresada == 'F': # Verifico que el usuario haya ingresado una ficha.
            cantidad_de_fichas -= 1 # En caso afirmativo resto una ficha a la cantidad ingresada por parámetro.
        else: print("Por favor solamente ingrese fichas reales (F)") # En otro caso muestro este mensaje.
    print("¡A jugar!") # Muestro un mensaje por pantalla.
 """
# Implementación inciso B:
""" 
def jugar_a_los_fichines_c2(cantidad_de_fichas): # Defino el encabezado de la función.
    while cantidad_de_fichas > 0: # Defino el encabezado del ciclo. Estableciendo que se repita su bloque de código hasta que la cantidad de fichas sea menor que cero.
        print(f"Ingresá {cantidad_de_fichas} fichas para comenzar.") # Se le pide al usuario que ingrese una ficha.
        opc_ingresada = input() # En este caso el input está separado para que sea mas prolijo pero la línea 217 y 218 podrían estar juntas en una sola.
        if opc_ingresada == 'F': # Verifico que el usuario haya ingresado una ficha.
            cantidad_de_fichas -= 1 # En caso afirmativo resto una ficha a la cantidad ingresada por parámetro.
        else: print("Por favor solamente ingrese fichas reales (F)") # En otro caso muestro este mensaje.
    print("¡A jugar!") # Muestro un mensaje por pantalla.
 """
# Enunciado:
""" 
Crear una función que reciba un número entero e imprima los números primos entre 0 y el número ingresado.
 """
# Implementación:
""" 
import math # Importo la biblioteca math para utilizar la raíz cuadrada.
def es_primo(numero): # Defino el encabezado de una función auxiliar.
    res = True # Defino una variable con un valor booleano.
    divisor = 2 # Defino una variable con el valor numérico 2
    while divisor <= math.sqrt(numero): # Defino el encabezado del ciclo. Estableciendo que se repita su bloque de código hasta que el divisor sea menor que la raíz cuadrada del número ingresado por parámetro.
        if numero % divisor == 0: # Verifico que el divisor divide al número ingresado por parámetro.
            res = False # En caso afirmativo alterno el valor de verdad de la variable definida anteriormente.
        divisor += 1 # En cualquier caso incremento en uno el valor del divisor.
    return res # Retorno el valor de verdad que me indica si el número ingresado es primo o no.

def imprimir_primos(numero): # Defino el encabezado de la función.
    for i in range(2, numero + 1): # Defino el encabezado del ciclo. Estableciendo una sucesión de números desde el 2 hasta número.
        if es_primo(i): # Verifico que el número sea primo, con la función auxiliar de antes.
            print(i) # En caso afirmativo lo muestro.
 """
# Aclaraciones:
""" 
1. Los imports siempre deben estar definidos en las primeras líneas de código, porque cualquier función 
que este por arriba de esta definición no podrá utilizar la biblioteca. Por ejemplo la función 
jugar_a_los_fichines_c2 no puede utilizar la biblioteca Math. Pero, como esto es una guía y solo se 
utiliza la biblioteca en este enunciado, me parecio mas prolijo definirlo al comienzo del ejercicio.

2. En la función es_primo utilizo la idea de la división por prueba hasta la raíz cuadrada. Esta idea
dice que si un es compuesto entonces alguno de sus factores es menor a su raíz cuadrada, en el caso 
de que todos los cocientes sean distintos de cero entonces el número es primo. Tome la decisión de 
utilizar este mecanismo porque es mas eficiente que verificar todos los números entre 2 y el ingresado.
Por ejemplo, para la llamada es_primo(15) el while daría 14 vueltas, pero usando el mecanismo da solo 2
dado que la raíz cuadrada de 15 es 3.87.
"""