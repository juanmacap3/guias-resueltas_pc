""" 
===============================
Si es la primera vez que abrís uno de estos archivos te recomiendo mirar el readme.
===============================
 """

# Enunciado
""" 
A lo largo del cuatrimestre vamos a ver cómo podemos darle instrucciones a la computadora,
a medida que vayamos aprendiendo a programar. Una vez visto el tutorial de Replit,
realice su primer programa: hacer que se imprima por pantalla un “¡Hola mundo!”.
Ayuda: escribir print(“¡Hola mundo!”) y darle play (Run).
En Visual Studio Code el botón esta arriba a la derecha, el triangulito.
(En Windows con CTRL+ALT+N también podes correrlo).
 """
# Implementación:
print("¡Hola mundo!")

# Enunciado
""" 
Esta semana vimos que cuando programamos podemos guardar datos en variables.
Teniendo en cuenta esto y recordando el concepto de variable que se estudió esta semana,
guardar el texto “¡Hola mundo!” en una variable e imprimir el texto usando esa variable.
 """
# Implementación:
saludo = "¡Hola mundo!" # Guardo en una variable el string "¡Hola mundo!".
print(saludo) # Lo muestro por pantalla.

# Enunciado
""" 
Crear otro programa que guarde un número en una variable, y luego lo imprima por pantalla,
como hicimos con el “¡Hola mundo!” del ejercicio 2, sólo que ahora hay que poner el nombre
de la variable en lugar del “¡Hola mundo!”.
 """
# Implementación:
numero = int(input("Ingrese un número: ")) # Pido un número al usuario.
print(numero) # Lo muestro por pantalla.
# Aclaración
""" 
input() guarda la entrada como un string. Por ejemplo si el usuario ingresa un 7, se guarda como el texto "7" no el número 7.
int() convierte el texto entre los parentesis en un número.
Por eso escribí int(input(...))
 """
# Enunciado
""" 
Vamos con otro un poco más complejo. Para el siguiente programa a realizar, se pide hacer dos variables
que guarden dentro números, y luego sumarlos. El resultado se tendrá que guardar en otra variable, y luego
imprimir este resultado.
 """
# Implementación:
numero = int(input("Ingrese el primer término de la suma ")) # Le pido al usuario un primer número.
otro_numero = int(input("Ingrese el segundo término de la suma ")) # Le pido al usuario un segundo número.
resultado = numero + otro_numero # Guardo en una variable la suma de los números.
print(resultado) # La muestro por pantalla.

# Enunciado
""" 
¿Te animás a probar el programa del ejercicio anterior con otras operaciones aritméticas y
combinándolas? Es decir, probar combinando la suma, división, resta y multiplicación. ¿Y con
más variables?
 """
# Implementación:
# Le pido al usuario dos números.
primer_numero = int(input("Ingrese un primer número: "))
segundo_numero = int(input("Ingrese un segundo número: "))

# Guardo en distintas variables algunas operaciones entre ellos.
diferencia = primer_numero - segundo_numero
producto = primer_numero * segundo_numero
division = primer_numero / segundo_numero
resto = primer_numero % segundo_numero # Este operador devuelve el resto de la división.

# Muestro por pantalla el valor de cada variable, es decir el resultado de cada operación.
print("Esta es la resta entre los números ingresados: ", diferencia)
print("Este es el producto entre los números ingresados: ", producto)
print("Esta es la división entre los números ingresados: ", division)
print("Este es el resto entre los números ingresados: ", resto)

# Aclaración:
""" 
Otras formas de mostrar por pantalla texto concatenado con variables son las siguientes.
print('Este es el producto entre los números ingresados:', producto)
print(f"Esta es la división entre los números ingresados: {division}")
print(f'Este es el resto de dividir {primer_numero} entre {segundo_numero}: {resto}')
 """