""" 
===============================
Si es la primera vez que abrís uno de estos archivos te recomiendo mirar el readme.
===============================
 """

# Enunciado:
""" 
Crear un programa que le solicite al usuario un entero y lo imprima por pantalla.
Recuerde que puede usar las funciones input (para solicitar información) y print para mostrar información.
 """
# Implementación:
""" 
numero = int(input("Ingrese un número entero ")) # Le pido al usuario un número.
print(numero) # Lo muestro por pantalla.
 """
# Enunciado:
""" 
Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
la suma de ambos números
la resta de ambos números
la multiplicación de ambos números
la división entera de ambos números
el resto
Más adelante podríamos crear nuestra propia calculadora :)
 """
# Implementación:
""" 
# Le pido al usuario dos números:
primer_numero = int(input("Ingrese un primer número entero: "))
segundo_numero = int(input("Ingrese un segundo número entero: "))

# Guardo en distintas variables algunas operaciones entre ellos.
suma = primer_numero + segundo_numero
diferencia = primer_numero - segundo_numero
producto = primer_numero * segundo_numero
division = primer_numero // segundo_numero
resto = primer_numero % segundo_numero

# Muestro por pantalla el valor de cada variable, es decir el resultado de cada operación.
print(suma)
print(diferencia)
print(producto)
print(division)
print(resto)
 """
# Una manera mas elegante de mostrar las operaciones es la siguiente:
""" 
print(f"{primer_numero} + {segundo_numero} = {suma}")
print(f"{primer_numero} - {segundo_numero} = {diferencia}")
print(f"{primer_numero} * {segundo_numero} = {producto}")
print(f"{primer_numero} / {segundo_numero} = {division}") # división guarda el valor de la división entera pero aca muestro por pantalla el símbolo de división decimal, porque la división entera no tiene un símbolo.
print(f"El resto de dividir {primer_numero} entre {segundo_numero} = {resto}")
 """

# Enunciado:
""" 
Crear un programa que le solicite al usuario un entero y determine si es par,
mostrando por pantalla un mensaje que indique el resultado.
Para determinar si un número es par o impar, se puede determinar con el uso del operador %,
les dejamos a ustedes el cómo.
 """
# Implementación:
""" 
numero_a_evaluar = int(input("Ingrese un número entero que quiera evaluar si es o no par: ")) # Le pido al usuario un número.
if (numero_a_evaluar % 2 == 0): # Verifico si el número ingresado es par o no, igualando su resto al dividir por dos con cero.
    print("El número ingresado es un número entero par") # Muestro un mensaje por pantalla para el caso en el que el número sea par.
else:
    print("El número ingresado es un número entero impar") # Muestro un mensaje por pantalla para el caso en el que el número sea impar.
 """
# Aclaración:
""" 
El contenido dentro del parentesis despues de la palabra reservada "if" es la condición de 
la estructura de control. La condición puede (o no) estar dentro de los parentesis, 
cuando la condición es compleja se suele encerrarla entre parentesis.
 """
# Enunciado:
""" 
 Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad tenía el usuario en el año ingresado.
 """
# Implementación:
""" 
anio_nacimiento = int(input("Ingrese su año de nacimiento: ")) # Le pido al usuario su año de nacimiento.
anio_auxiliar = int(input("Ingrese cualquier otro año: ")) # Le pido al usuario un año cualquiera.
calculo_edad = anio_auxiliar - anio_nacimiento # Calculo la edad del usuario en el año ingresado.

print("Tu edad en el año", anio_auxiliar, " sería ", calculo_edad, "años.") # Muestro por pantalla la edad del usuario en el año ingresado.
 """
# Enunciado:
""" 
Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos.
Es muy común usar variables para acumular valores.
 """
# Implementación:
""" 
# Le pido al usuario los cinco números
primer_numero = int(input("Ingrese un primer número: "))
segundo_numero = int(input("Ingrese un segundo número: "))
tercer_numero = int(input("Ingrese un tercer número: "))
cuarto_numero = int(input("Ingrese un cuarto número: "))
quinto_numero = int(input("Ingrese un quinto número: "))

promedio = (primer_numero + segundo_numero + tercer_numero + cuarto_numero + quinto_numero) / 5 # Calculo el promedio entre los números.

print("El promedio entre los números ingresados es ", promedio) # Lo muestro por pantalla.
 """
# Aclaración:
""" 
Otra manera de mostrarlo podría ser la siguiente.
print(f"El promedio entre los números ingresados es {promedio}") # Lo muestro por pantalla.
 """
# Enunciado:
""" 
Crear una función que reciba un número y muestre el anterior y el siguiente.
 """
# Implementación:
""" 
def mostrar_en_escalera(numero): # Defino el encabezado, o firma, de la función.
    numero_anterior = numero - 1 # Calculo el número anterior al ingresado por parámetro.
    numero_siguiente = numero + 1 # Calculo el número siguiente al ingresado por parámetro.
    print(numero_anterior)
    print(numero_siguiente)
 """
# Caso de uso
""" 
mostrar_en_escalera(7)
 """
# Enunciado
""" 
 Crear una función que una un string y un entero.
 """
# Implementación:
""" 
def concatenar_texto_con_numero(texto, numero): # Defino el encabezado de la función.
    texto += str(numero) # Concateno, o uno, el string con el número.
    print(texto)
 """
# Aclaraciones:
""" 
1. La concatenación también podría ser texto = texto + str(numero).
2. Es necesario alterar el tipo de dato del número porque sino estariamos sumando un número a un string, lo cual no tiene sentido.
 """
# Caso de uso
""" 
concatenar_texto_con_numero("Guido", 7)
 """
# Enunciado:
""" 
Crear una función que reciba un entero y que retorne el resto y el cociente.
 """
# Aclaración:
"""
Al no especificar contra que número debo calcular el resto y el cociente lo voy a hacer contra 2
 """
# Implementación:
""" 
def resto_cociente_de_un_numero(numero):
    resto = numero % 2 # Calculo el resto.
    cociente = numero // 2 # Calculo el cociente.
    return resto, cociente # Los retorno, o devuelvo.
 """
# Caso de uso
""" 
resto_cociente_de_un_numero(7)
 """
# Enunciado:
""" 
Pedirle nombre y apellido por separado e imprimir “Apellido, Nombre”.
Este proceso se llama concatenar cadenas.
 """
# Implementación:
""" 
nombre_ingresado = input("Ingrese su nombre: ") # Le pido al usuario su nombre.
apellido_ingresado = input("Ingrese su apellido: ") # Le pido al usuario su apellido.
nombre_completo = nombre_ingresado + " " + apellido_ingresado # Concateno los nombres.
print(nombre_completo) # Muestro el string.
 """
# Enunciado:
""" 
Obtener una palabra e imprimir la cantidad de letras.
 """
# Implementación:
""" 
palabra_para_contarle_las_letras = input("Ingrese una palabra: ") # Le pido al usuario una palabra.
print(len(palabra_para_contarle_las_letras)) # Uso la función integrada de Python para contar las letras de la palabra.
 """
# Enunciado:
""" 
Obtener una palabra e imprimir los primeros 5 caracteres.
 """
# Implementación:
""" 
sub_palabra = input("Ingrese una palabra, se mostran los primeros 5 caracteres: ") # Le pido al usuario una palabra.
print(sub_palabra[0:5]) # Muestro las primeras cinco letras.
 """
# Enunciado:
""" 
 Obtener una palabra, borrarle todas las ‘a’ e imprimirla por pantalla.
 """
# Implementación:
sub_palabra = input("Ingrese una palabra, se le borraran las a que contenga: ") # Le pido al usuario una palabra.
sub_palabra_aux = "" # Defino un string vacío.
if 'a' in sub_palabra: # Verifico que la palabra contenga la letra a.
    for i in range(len(sub_palabra)): # Recorro la palabra, letra por letra.
        if sub_palabra[i] != 'a': # Verifico si la letra no es la a.
            sub_palabra_aux += sub_palabra[i] # Si la letra no es una a, la agrego al string vacío que definí antes.
    sub_palabra = sub_palabra_aux # Sobreescribo el valor de la palabra ingresada por la que no tiene a.
print(sub_palabra) # Lo muestro por pantalla.
