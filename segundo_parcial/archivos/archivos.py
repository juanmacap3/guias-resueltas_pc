""" 
===============================
Si es la primera vez que abrís uno de estos archivos te recomiendo mirar el readme.
===============================
 """

# Enunciado
""" 
Se tiene un archivo con la pregunta "¿Cómo estás hoy?" llamado pregunta.txt. Se pide leerlo y mostrar
la pregunta por pantalla para luego pedirle al usuario que ingrese una respuesta. Después, guardar la
respuesta dada por el usuario en el archivo.
Por ejemplo, se tiene el archivo pregunta.txt que originalmente tiene:
¿Cómo estás hoy?
Y el usuario de la respuesta: "¡Bien, porque me comí una hamburguesa!"
Entonces el archivo debería quedar de la forma:
¿Cómo estás hoy?
¡Bien, porque me comí una hamburguesa!
 """
# Implementación:
""" 
archivo = open("arc.txt", 'r') # Abro el archivo en modo lectura 
contenido_archivo = archivo.read() # Guardo el contenido del archivo.
archivo.close() # Cierro el archivo
respuesta = input(contenido_archivo) # Le pregunto al usuario como está.
archivo = open("arc.txt", 'a') # Abro el archivo con modo agregar.
archivo.write('\n' + respuesta) # Escribo en el archivo la respuesta del usuario.
archivo.close() # Cierro el archivo.
 """
# Enunciado.
""" 
En un archivo llamado regalo.txt se tiene la lista de las personas que quieren participar en el regalo de
cumpleaños de Sol (en cada línea está el nombre de una persona). El encargado de organizar el regalo
es Ale, y quiere saber más información antes de ir a comprarle algo a Sol.
    a. Mostrar por pantalla los nombres de las personas que quieren participar en el regalo.
    b. Se sabe que quieren poner 1000 pesos por persona por regalo. Hacer una función que devuelva
        cuánto dinero tiene Ale para hacerle el regalo a Sol. Es decir si se tiene un archivo de esta
        forma:
        Agus
        Manu
        Santi
        Lorena
        Maria
        La función tiene que devolver 5000
    c. Tomi sabe que si participa Santi, también participa Tomi. Se pide que si Santi está en el archivo
    de los nombres, se agregue también a Tomi.
 """
# Implementación inciso A:
""" 
archivo = open("arc.txt", 'r') # Abro el archivo en modo lectura.
contenido_archivo = archivo.readlines() # Guardo el contenido del archivo.
archivo.close() # Cierro el archivo.
for nombre in contenido_archivo: # Defino el encabezado del ciclo. Recorriendo el contenido del archivo nombre a nombre.
    print(nombre) # Muestro el nombre y el ciclo vuelve al encabezado.
 """
# Implementación inciso B.
"""
La idea va a ser generar una lista con los nombres, las lineas del archivo, y a la longitud de la lista multiplicarle 1000.
 """
""" 
def calcular_monto(ruta): # Defino el encabezado de la función.
    archivo = open(ruta, 'r') # Abro el archivo en modo lectura.
    contenido_archivo = archivo.readlines() # Guardo el contenido del archivo.
    archivo.close() # Cierro el archivo.
    monto = len(contenido_archivo) * 1000 # Calculo el monto.
    return monto # Retorno el monto que tiene Ale para hacerle el regalo a Sol.
 """
# Implementación inciso C.
""" 
La idea va a ser verificar que santi este, en ese caso agregar al archivo el nombre tomi
 """
""" 
archivo = open("arc.txt", 'r') # Abro el archivo en modo lectura.
contenido_archivo = archivo.readlines() # Guardo el contenido del archivo.
archivo.close() # Cierro el archivo.
for nombre in contenido_archivo: # Defino el encabezado del ciclo. Recorriendo la lista de nombres, nombre por nombre.
    if nombre.lower().strip() == "santi":  # Verifico si Santi está en el archivo.
        # En ese caso abro el archivo, agrego a Tomi al final y lo cierro.
        archivo = open("arc.txt", 'a')
        archivo.write("\nTomi")
        archivo.close()
 """
# Enunciado:
""" 
En un hogar se quieren organizar mejor con las compras, por lo que se quiere guardar en un archivo la
lista de productos que se necesitan para la próxima vez que la familia vaya al supermercado. Se pide
hacer un programa que cree un archivo de compras.txt (Ayuda: abrir el archivo en modo w) y le
pregunte al usuario qué necesita comprar hasta que ingrese una X. Por ejemplo:
> ¿Qué agrego a la lista de compras?
> Papa
> ¿Qué agrego a la lista de compras?
> Pollo
> ¿Qué agrego a la lista de compras?
> Fideos
> ¿Qué agrego a la lista de compras?
> X
El archivo tendría que estar de la siguiente forma:
Papa
Pollo
Fideos
 """
# Implementación:
""" 
La idea va a ser preguntarle al usuario que hay que comprar, guardarlo en una lista y escribir todos los productos, luego cerrar el archivo.
 """
""" 
productos = [] # Defino una lista vacía.
producto = input("¿Que agrego a la lista de compras? Ingrese 'X' para terminar: ") # Le pido al usuario un producto.
while producto.upper() != 'X': # Defino el encabezado del ciclo. Estableciendo que se repita mientras el producto, todo escrito en mayúsculas, sea distinto a 'X'.
    productos.append(producto+'\n') # Agrego el producto con un salto de línea.
    producto = input("¿Que agrego a la lista de compras? Ingrese 'X' para terminar: ") # Le pido otro producto al usuario y el ciclo vuelve a su encabezado.
archivo = open("arc.txt", 'w') # Abro el archivo en modo escritura.
archivo.writelines(productos) # Escribo todos los productos.
archivo.close() # Cierro el archivo.
 """
# Enunciado
""" 
Se tiene un archivo con el siguiente texto:

Paco Peco, chico rico,
insultaba como un loco
a su tío Federico;
y éste dijo: Poco a poco,
Paco Peco, poco pico. Me han dicho que has dicho un dicho
que han dicho que he dicho yo,
el que lo ha dicho, mintió,
y en caso que hubiese dicho
ese dicho que tú has dicho
que han dicho que he dicho yo,
dicho y redicho quedó.
y estaría muy bien dicho,
siempre que yo hubiera dicho
ese dicho que tú has dicho
que han dicho que he dicho yo.

Se pide hacer un programa que pida dos palabras: una que se quiera reemplazar y la palabra por la que
se quiera reemplazar, cambie el texto y lo guarde en el archivo otra vez. Por ejemplo, si la función
recibe "poco" y "mucho", reemplaza "poco" por "mucho" todas las veces que aparezca en el texto.
 """
# Implementación
""" 
La idea va a ser generar un string con todo el contenido del archivo, pedirle al usuario las palabras, editar el string y reescribir el archivo.
 """
""" 
archivo = open("arc.txt", 'r') # Abro el archivo en modo apertura.
contenido_archivo = archivo.read() # Guardo el contenido del archivo en un string.
archivo.close() # Cierro el archivo.

palabra_a_reemplazar = input("Ingrese la palabra que quiere reemplazar: ") # Le pido al usuario la palabra que quiere reemplazar.
palabra_para_reemplazar = input("Ingrese la palabra por la que quiere reemplazar: ") # Le pido al usuario la palabra por la que quiere reemplazar.
contenido_archivo = contenido_archivo.replace(palabra_a_reemplazar, palabra_para_reemplazar) # Edito el contenido del archivo.

archivo = open("arc.txt", 'w') # Abro el archivo en modo escritura.
archivo.write(contenido_archivo) # Sobreescribo el archivo.
archivo.close() # Cierro el archivo.
 """
# Enunciado
""" 
Se tiene un archivo csv que contiene información sobre el stock de una librería. Se guarda por cada
línea, el nombre del producto, el código, el precio por unidad y el stock actual, es decir:
nombre;código;precio;stock
Un posible ejemplo de este archivo es el siguiente:
lapiceras;34512;50;120
cuadernos;41611;500;130
sacapuntas;62812;30;210
…

Se pide:
    a. Leer el archivo y mostrarlo por pantalla con el siguiente formato:
    Nombre producto: lapiceras
    Código producto: 34512
    Precio por unidad: 50
    Stock: 120
    Nombre producto: cuadernos
    Código producto: 41611
    Precio por unidad: 500
    Stock: 130
    …
    b. Hacer una función que reciba un diccionario que describa una línea del archivo y lo agregue, es
    decir que si se recibe un diccionario del tipo
    {
    "nombre": "hojas A4",
    "código": 35662,
    "precio": 600,
    "stock": 45
    }
 """
# Implementación inciso A
""" 
La idea es leer el archivo y recorrerlo.
 """
""" 
archivo = open("arc.csv", 'r') # Abro el archivo en modo lectura.
contenido_archivo = archivo.readlines() # Genero una lista con el contenido del archivo.
archivo.close() # Cierro el archivo.

for i in range(1, len(contenido_archivo)): # Defino el encabezado del ciclo. Estableciendo una sucesión de números desde el 1 hasta la cantidad de elementos de la lista contenido_archivo menos uno.
    producto = contenido_archivo[i].split(';') # Separo los substring de un elemento de la lista contenido_archivo, usando como separador el carácter ';'. Estos substrings los guardo en otra lista de strings.
    # Accedo a las posiciones de la lista que generé en la línea anterior.
    print("Nombre producto: " + producto[0])
    print("Código del producto: " + producto[1])
    print("Precio por unidad: " + producto[2])
    print("Stock: " + producto[3])
 """
# Implementación inciso B.
""" 
La idea va a ser definir la función, leer la información del diccionario y agregarla al archivo.
 """
""" 
def agregar_producto(producto): # Defino el encabezado de la función.
    txt = "" # Defino un string vacío.
    for clave in producto: # Defino el encabezado del ciclo. Recorriendo el diccionario clave a clave.
        txt += str(producto[clave]) + ";" # Al string vacío le agrego los valores del diccionario separados por ';'.
    txt = txt[0:-1] # Le saco al string con los valores del diccionario el último ';'.
    archivo = open("arc.csv", 'a') # Abro el archivo en modo agregar.
    archivo.write("\n" + txt) # Escribo el string en el archivo.
    archivo.close() # Cierro el archivo.
 """
# Enunciado
""" 
Una profesora tiene una lista de diccionarios para guardar las notas que sacaron sus alumnos en el
último parcial que tomó. Cada uno de esos diccionarios tiene el nombre del alumno, su apellido, su dni
y la nota que sacó.
    a. Hacer una función que reciba este diccionario, y guarde las notas en un archivo csv, llamados
    notas.csv
    b. Tiempo después de guardar las notas, la profesora quiso saber la cantidad de alumnos que
    aprobaron. Hacer una función que lea el archivo creado en el ejercicio anterior, y devolver la
    cantidad de alumnos aprobados (su nota es mayor a 4).
 """
# Implementación del inciso A.
""" 
La idea es definir la función, que recibe la lista de diccionarios, recorrerla (para leer la información de los diccionarios) y escribir la información en el archivo.
 """
""" 
def escribir_notas(alumnos): # Defino el encabezado de la función, alumnos es una lista.
    contenido_archivo = "Nombre;Apellido;DNI;Nota\n" # Defino un string, el cual es la cabecera de la tabla.
    for alumno in alumnos: # Defino el encabezado del primer ciclo. Recorriendo la lista, de diccionarios, diccionario a diccionario.
        for clave in alumno: # Defino el encabezado del ciclo anidado. Recorriendo el diccionario clave a clave.
            contenido_archivo += str(alumno[clave]) + ';' # Al string definido anteriormente le agrego la información del diccionario, separandolo por ';'. Luego vuelve al encabezado del ciclo anidado.
        contenido_archivo = contenido_archivo[0:-1] # Al string le saco el último carácter, un ';' innecesario.
        contenido_archivo += '\n' # Al string le agrego al final un salto de línea. Luego vuelve al encabezado del primer ciclo.
    archivo = open("arc.csv", 'w') # Abro el archivo en modo escritura.
    archivo.write(contenido_archivo) # Escribo el string con la infor
    archivo.close() # Cierro el archivo.
 """
# Implementación del inciso B.
""" 
La idea va a ser leer el archivo y acceder al último carácter de cada línea del archivo, el cual es la nota de los alumnos.
 """
""" 
def cant_alums_aprobados(): # Defino el encabezado de la función.
    alumnos_aprobados = 0 # Defino una variable para contar la cantidad de alumnos aprobados.
    archivo = open("arc.csv", 'r') # Abro el archivo en modo lectura.
    contenido_archivo = archivo.readlines() # Genero una lista con el contenido del archivo.
    for i in range(1, len(contenido_archivo)): # Defino el encabezado del ciclo. Estableciendo una sucesión de números desde 1 hasta la longitud de la lista menos uno.
        alumno = contenido_archivo[i].split(';') # Separo los substring de un elemento de la lista contenido_archivo, usando como separador el carácter ';'. Estos substrings los guardo en otra lista de strings.
        if int(alumno[-1]) > 4: # Verifico si el último elemento de la lista, la nota del alumno, es mayor a cuatro.
            alumnos_aprobados += 1 # En ese caso incremento en uno el contador de alumnos aprobados y el ciclo vuelve al encabezado.
    return alumnos_aprobados # Retorno la cantidad de alumnos aprobados.
 """
# Enunciado
""" 
En un cine tienen dos archivos .txt, uno con salas y otro con nombres de películas. Se sabe que en la
sala de una fila del archivo se va a transmitir la película de la misma fila del archivo de películas. Se pide
leer los dos archivos, y crear un nuevo archivo csv que tenga el nuevo formato sala;pelicula
Por ejemplo si se tienen los siguientes archivos:
(salas.txt) (peliculas.txt)
D2          Megamente
F1          Rápidos y furiosos
E4          El padrino
El nuevo archivo deberá quedar:
(funciones.csv)
D2;Megamente
F1;Rápidos y furiosos
E4;El padrino
 """
# Implementación
""" 
La idea va a ser leer los dos archivos y recorrerlos simultaneamente.
 """
""" 
# Leo el contenido de los archivo salas y peliculas, y cierro los dos archivos.
salas = open("salas.txt", 'r')
contenido_salas = salas.readlines()
salas.close()
peliculas = open("peliculas.txt", 'r')
contenido_peliculas = peliculas.readlines()
peliculas.close()

# Defino un string vacío.
contenido_funciones = ""

for i in range(len(contenido_salas)): # Defino el encabezado del ciclo. Estableciendo una sucesión de números desde cero hasta la longitud de la lista menos uno.
    contenido_funciones += contenido_salas[i].strip() + ";" + contenido_peliculas[i] # Agrego en el string vacío el contenido de los archivos.

funciones = open("funciones.csv", 'w') # Abro el archivo funciones en modo escritura.
funciones.write(contenido_funciones) # Escribo el contenido en el formato solicitado.
funciones.close() # Cierro el archivo.
 """
# Enunciado
""" 
Santi le fue mostrando colores a sus amigos y cada amigo le fue diciendo si le gusta o no. Guardó cada
respuesta en un .csv de la siguiente manera: nombre;color;le gusta, pero se dió cuenta que no es una
forma muy práctica de guardarlo, así que lo quiere cambiar. Hacer un programa que lea el archivo y lo
transforme en un archivo .txt. Es decir que si se tiene un archivo csv de la siguiente forma:
Agus;verde;si
Tomi; violeta;no
Manu;marrón;si
El archivo .txt tiene que quedar así:
A Agus sí le gusta el verde
A Tomi no le gusta el violeta
A Manu sí le gusta el marrón
 """
# Implementación
""" 
archivo = open("arc.csv", 'r') # Abro el archivo csv en modo lectura.
contenido_archivo_csv = archivo.readlines() # Guardo el contenido del archivo en una lista de strings.
archivo.close() # Cierro el archivo csv.

contenido_archivo_txt = "" # Defino un string vacío.

for linea_csv in contenido_archivo_csv: # Defino el encabezado del ciclo. Recorriendo la lista, de strings, string por string.
    linea_txt = linea_csv.split(';') # A cada string lo convierto en una lista de strings, compuesta por substrings del elemento de la lista.
    if "si" in linea_txt[-1]: # Verifico si en el último elemento de está nueva lista ésta la palabra si.
        contenido_archivo_txt += "A "+ linea_txt[0] + " sí le gusta el " + linea_txt[1] + '\n' # En ese caso agrego al string vacío que definí antes este string.
    else:
        contenido_archivo_txt += "A "+ linea_txt[0] + " no le gusta el " + linea_txt[1] + '\n' # En otro caso agrego este otro string.

archivo = open("arc.txt", 'w') # Abro el archivo txt en modo escritura.
archivo.write(contenido_archivo_txt) # Escribo el string con la información del archivo csv.
archivo.close() # Cierro el archivo txt.
 """