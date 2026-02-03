""" 
===============================
Si es la primera vez que abrís uno de estos archivos te recomiendo mirar el readme.
===============================
 """

# Enunciado
""" 
En una escuela se quiere tener un sistema para guardar la información de sus estudiantes para tener
mejor organizado sus datos.
    a. Crear un diccionario que sirve para representar a una persona en este contexto, pensar en las
        características que se consideren más relevantes para identificar a una persona (su nombre,
        DNI, edad, etc).
    b. Agregar al diccionario creado, un campo que sea otro diccionario y sirva para guardar el curso
        del estudiante y sus características (año, división, orientación, etc).
    c. Teniendo una lista de diccionarios de estudiantes, buscar en la lista la persona con mayor edad
        e imprimirla por pantalla.
 """
# Implementación inciso a.
# Defino un diccionario.
""" 
alumno1 = { 
    "nombre" : "Nestor",
    "apellido" : "Rossi",
    "edad" : 28,
    "DNI" : 11111111,
    "num_libreta" : "000/00"
}
 """
# Implementación inciso b.
""" 
alumno1["info_estudiantil"] = {
    "anio" : 1,
    "comisión" : 3344,
    "carrera" : "Lic. en cs. de la computación",
    "materias" : ["Física", "Álgebra", "Pensamiento computacional"],
    "CBC" : True
}
 """
# Implementación inciso c.
""" 
edad_max = 0 # Defino una variable que representa la edad maxima entre los alumnos.
posicion_alum_mas_grande = 0 # Defino una variable que representa la posición en la que se encuentra el alumno mas grande.

# Defino dos alumnos (diccionarios) y una lista de alumnos (diccionarios), teniendo en cuenta al definido en el inciso a.
alumno2 = { 
    "nombre" : "Sabrina",
    "apellido" : "Suarez",
    "edad" : 21,
    "DNI" : 11111112,
    "num_libreta" : "010/00"
}

alumno3 = { 
    "nombre" : "Guadalupe",
    "apellido" : "Solá",
    "edad" : 31,
    "DNI" : 11141111,
    "num_libreta" : "200/00"
}

alumnos = [alumno1, alumno2, alumno3]

for i in range(len(alumnos)): # Defino el encabezado del ciclo. Estableciendo una sucesión de números desde cero hasta la longitud de la lista menos uno.
    if edad_max < alumnos[i]["edad"]: # Verifico si la edad del alumno es mayor que la edad maxima definida anteriormente.
        # En ese caso actualizo las variables definidas al comienzo del ejercicio con la información del alumno mas grande.
        edad_max = alumnos[i]["edad"]
        posicion_alum_mas_grande = i

print(alumnos[posicion_alum_mas_grande]) # Muestro por pantalla al alumno mas grande.
 """

# Enunciado
""" 
En un vivero se guardan las plantas en una lista de diccionario con la siguiente información: especie, si
necesita luz solar o no, y el precio. (OBSERVACIÓN: ¿Qué tipo de dato nos permitía guardar si algo es
verdad o no?). Ahora se necesita un sistema que guarde las plantas a medida que van llegando. Se pide
hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva y agregue
esa planta a la lista de diccionarios.
 """
# Implementación
""" 
def agregar_planta(plantas, especie_planta_nueva, luz_planta_nueva, precio_planta_nueva): # Defino el encabezado de la función
    # Defino un diccionario con la información de la planta nueva.
    nueva_planta = {
        "especie" : especie_planta_nueva,
        "necesita_luz" : luz_planta_nueva,
        "precio" : precio_planta_nueva
    }
    plantas.append(nueva_planta) # Agrego el diccionario a la lista de diccionarios pasada por parámetro.
 """
# Caso de uso
""" 
libro = [
    {
        "especie" : "Jazmin del cielo",
        "necesita_luz" : True,
        "precio" : 4220.21
    },
    {
        "especie" : "Jacaranda",
        "necesita_luz" : True,
        "precio" : 31210.71
    }
]

agregar_planta(libro, "Rosa", True, 44640.56)
 """
# Enunciado
""" 
Se representa un ticket de supermercado como una lista de diccionarios, donde cada diccionario tiene
la siguiente información:
    ● Nombre del producto
    ● Precio por unidad
    ● Cantidad
Se pide hacer una función que reciba el ticket y devuelva el monto total a pagar.
 """
# Implementación
""" 
def total_compra(ticket): # Defino el encabezado de la función, ticket es una lista de diccionarios.
    total = 0 # Defino una variable numérica para guardar el total a pagar de la compra.
    for producto in ticket: # Defino el encabezado del ciclo. Recorriendo el ticket, producto por producto.
        total += producto["precio_unitario"] * producto["cantidad"] # A la variable definida anteriormente le agrego la multiplicación entre el precio unitario y la cantidad, luego el ciclo vuelve a su encabezado.
    return total # Devuelvo el total de la compra.
 """
# Caso de uso
"""
producto1 = {
    "nombre" : "Cafe",
    "precio_unitario" : 8799.99,
    "cantidad" : 21
}

producto2 = {
    "nombre" : "Yerba mate",
    "precio_unitario" : 4399.99,
    "cantidad" : 47
}

producto3 = {
    "nombre" : "Te negro",
    "precio_unitario" : 2199.99,
    "cantidad" : 14
}

productos = [producto1, producto2, producto3]

print(total_compra(productos))
 """
# Enunciado
""" 
Sol tiene una lista de diccionarios donde guarda todas las películas que vió. La información que tiene
para cada una es: el nombre de la serie, año en que salió, y la puntuación que le puso del 1 al 10. Hace
mucho que quiere que Tomás empiece a ver las películas que ella considera que son las mejores que
vio.
Hacer una función que reciba el diccionario de las películas que vió Sol, y que devuelva una nueva lista
de diccionarios donde sólo estén las películas que tienen puntaje mayor a 7.
 """
# Implementación
""" 
def filtrar_mejores_peliculas(peliculas): # Defino el encabezado de la función, peliculas es una lista de diccionarios.
    mejores_peliculas = [] # Defino una lista vacía.
    for pelicula in peliculas: # Defino el encabezado del ciclo. Recorriendo las peliculas (lista de diccionarios) pelicula (diccionario) a pelicula (diccionario)
        if pelicula["puntaje"] > 7: # Verifico si la película tiene un puntaje mayor a 7.
            mejores_peliculas.append(pelicula) # En ese caso lo agrego en la lista que definí anteriormente.
    return mejores_peliculas # Devuelvo la lista con las películas que tienen puntaje mayor a 7.
 """
# Caso de uso
""" 
pelicula1 = {
    "nombre" : "Kill Bill",
    "anio" : 2003,
    "puntaje" : 10.0
}

pelicula2 = {
    "nombre" : "Esperando la carroza",
    "anio" : 1985,
    "puntaje" : 6.0
}

pelicula3 = {
    "nombre" : "Dog Day Afternoon",
    "anio" : 1975,
    "puntaje" : 8.0
}

pelis = [pelicula1, pelicula2, pelicula3]

print(filtrar_mejores_peliculas(pelis))
 """
# Enunciado
""" 
Un profesor guarda las notas del primer parcial de sus alumnos en una lista de diccionarios que guarda
la siguiente información:
● Nombre
● Apellido
● Intento
● Nota
Donde ”intento” es la instancia que está rindiendo, 1 si es la primera vez que rinde el parcial, 2 si es el
primer recuperatorio y 3 si es el segundo recuperatorio.
Se pide hacer una función que, dado esta lista de diccionarios, devuelva el promedio de las notas en la
primera oportunidad que rindieron los alumnos.
¿Cómo harían para generalizar la función y que el intento sea parametrizable? Es decir, que no
solamente sirve para el intento 1, sino que también pueda servir para los demás
 """
# Implementación
""" 
Voy a hacer directamente la versión del intento parámetrizado. La idea va a ser contar la cantidad de 
alumnos que están en determinado intento, al mismo tiempo sumar las notas que tienen, y luego dividir 
la suma total de las notas por los alumnos que están en dicho intento.
 """
""" 
def promedio_por_intento(alumnos, intento): # Defino el encabezado de la función (alumnos es una lista de diccionarios e intento es un número).
    suma_total_notas = 0 # Defino una variable numérica para guardar la suma de todas las notas de los alumnos que estan en un mismo intento.
    cantidad_alumno_por_intento = 0 # Defino una variable numérica para guardar la cantidad de alumnos que están en un mismo intento.
    promedio = 0 # Defino una variable numérica para guardar el promedio de los alumnos que estan en un mismo intento.
    for alumno in alumnos: # Defino el encabezado del ciclo. Recorriendo los alumnos (lista de diccionarios) alumno (diccionario) por alumno (diccionario).
        if alumno["intento"] == intento: # Verifico si el intento del alumno es igual al que se ingreso por parámetro.
            suma_total_notas += alumno["nota"] # En ese caso agrego a una de las variables la nota del alumno.
            cantidad_alumno_por_intento += 1 # Y también incremento en uno la cantidad de alumnos que están en este intento.
    if cantidad_alumno_por_intento != 0: # Verifico que haya por lo menos algún alumno en el intento ingresado por parámetro (para evitar dividir por cero).
        promedio = suma_total_notas / cantidad_alumno_por_intento # En ese caso sobreescribo la variable por el calculo del promedio.
    return promedio # Devuelvo el promedio de los alumnos que comparten intento.
 """
# Aclaración
""" 
Si queres verificar si la implementación que hiciste, declarando al intento como 1, tiene el mismo resultado que la mia podes hacer dos cosas
1. Llamar a las dos funciones con la misma lista y al llamado de mi función le pasas un segundo argumento con el número 1.
2. Modificas mi implementación, sacando el segundo parámetro y editando la condición del primer condicional.
 """
# Caso de uso
""" 
alum1 = {
    "nombre" : "Juan Carlos",
    "apellido" : "Silva",
    "intento" : 1,
    "nota" : 4
}

alum2 = {
    "nombre" : "Lorena Salma",
    "apellido" : "Rodriguez",
    "intento" : 3,
    "nota" : 7
}

alum3 = {
    "nombre" : "Sulma Cristina",
    "apellido" : "Siley",
    "intento" : 1,
    "nota" : 5
}

alum4 = {
    "nombre" : "Gonzalo Matias",
    "apellido" : "Gimenez",
    "intento" : 1,
    "nota" : 8
}

alums = [alum1, alum2, alum3, alum4]

print(promedio_por_intento(alums, 1))
 """
# Enunciado
""" 
En una fábrica, se hace un chequeo de calidad a los productos antes de cada entrega. El resultado del
chequeo de la entrega se guarda en una lista de diccionarios, donde cada diccionario tiene la siguiente
información de cada producto:
● Código del producto
● Fecha de vencimiento
● Si pasó el chequeo de calidad o no
Se pide hacer una función que reciba esta lista de diccionarios y elimine todos los productos que no
pasaron el chequeo de calidad. Devolver en una tupla el diccionario con los elementos eliminados y la
cantidad de elementos que quedaron en el diccionario.
Dado que la tupla es inmutable y nosotros no podemos ir agregando elementos a una tupla, ¿En qué
momento deberíamos crear la tupla?
 """
# Implementación
""" 
La idea va a ser agregar los elementos en una lista y luego cambiarle el tipo de dato a una tupla.
 """
"""
def filtrar_productos_mala_calidad(productos): # Defino el encabezado de la función
    productos_mala_calidad = [] # Defino una lista vacía
    for i in range(len(productos)-1,-1,-1): # Defino el encabezado del ciclo. Recorriendo la lista de atras hacia adelante para eliminar los elementos sin problemas.
        if not productos[i]["calidad"]: # Verifico si la calidad del producto es falso.
            prod_mala_calidad = productos.pop(i) # En ese caso elimino el producto de la lista pasada por parámetro.
            productos_mala_calidad.append(prod_mala_calidad) # Agrego el elemento a la lista vacía que definí anteriormente y el ciclo vuelve a su encabezado.
    productos_mala_calidad = tuple(productos_mala_calidad) # Convierto la lista en una tupla.
    return productos_mala_calidad, len(productos_mala_calidad) # Devuelvo una tupla con la tupla que contiene los diccionarios que su control de calidad es falso y la cantidad de elementos que tiene dicha tupla de diccionarios.
 """
# Aclaración
""" 
La lista de productos la recorro de atras para adelante porque, al alterar el tamaño de la lista, 
voy a llegar a un punto que voy a tener un error de indice fuera de rango.
Por ejemplo, con una lista súper básica.
[{"calidad" : True},{"calidad" : False},{"calidad" : True}]
    Si recorro desde el primer elemento al último i == 0.
    En la primera ejecución no entramos al if, porque not productos[0]["calidad"] es falso.
    En la segunda ejecución, i == 1, entramos al if porque not productos[0]["calidad"] es verdadero, por lo tanto lo elimino de la lista.
    En este punto la lista quedo así: [{"calidad" : True},{"calidad" : True}]. O sea una lista de dos elementos, con índices 0 y 1.
    En la tercera vuelta, i == 2, pero en la lista no existe el elemento con índice 2, entonces se produce un error.
 """
# Caso de uso
""" 
producto1 = {
    "codigo" : "YENJ27",
    "vencimiento" : "07/2025",
    "calidad" : False
}

producto2 = {
    "codigo" : "JDYL89",
    "vencimiento" : "01/2025",
    "calidad" : False
}

producto3 = {
    "codigo" : "DU28NX",
    "vencimiento" : "07/2028",
    "calidad" : True
}

prods = [producto1, producto2, producto3]

print(filtrar_productos_mala_calidad(prods))
 """
# Enunciado
""" 
Se quiere guardar la información de un grupo de maratonistas. Se necesita guardar su nombre, DNI, y
todas las maratones que corrió, de la cual a su vez se quiere tener el nombre de cada una, el año, el
puesto en que salió el maratonista, y el tiempo que tardó en terminarla.
    a. Crear el diccionario que represente esta situación.
        AYUDA: Queremos guardar muchos maratonistas, y a su vez, muchas maratones para cada
        maratonista, entonces ¿Qué tipo de dato debería ser el campo que guarda todas las
        maratones? ¿Y qué tipo de dato es la maratón en sí?
    b. Teniendo una lista de diccionarios de maratonistas, ordenarlos alfabéticamente.
    c. Ordenar las maratones de cada maratonista según el tiempo que tardó en completar cada una
        de forma ascendente.
 """
# Respuesta del inciso a
""" 
El tipo de dato que almacena las maratones debe ser una lista de diccionarios, dado que cada maraton 
tiene varios datos con nombres especificos, lo cual es ideal para utilizar un diccionario para cada 
maraton. Luego para coleccionar las maratones, lo mejor es una lista.
 """
# Implementación inciso a
# Aclaración
""" 
Los tiempos van a estar medidos en segundos.
 """
# Defino cada uno de los maratonistas. Usando un diccionario para cada uno y una lista de diccionarios para sus maratones.
""" 
maratonista1 = {
    "nombre" : "Luigi Julma",
    "DNI" : "11111111",
    "maratones" : [{
        "nombre" : "Medio Maratón de Buenos Aires.",
        "anio" : 2017,
        "puesto" : 1,
        "tiempo" : 5101
    },
    {
        "nombre" : "Maratón Internacional de Buenos Aires.",
        "anio" : 2025,
        "puesto" : 3,
        "tiempo" : 10041
    }]
}

maratonista2 = {
    "nombre" : "Tavo Soria",
    "DNI" : "33333333",
    "maratones" : [{
        "nombre" : "Medio Maratón de Buenos Aires.",
        "anio" : 2017,
        "puesto" : 3,
        "tiempo" : 5483
    },
    {
        "nombre" : "Maratón Internacional de Buenos Aires.",
        "anio" : 2025,
        "puesto" : 1,
        "tiempo" : 8034
    }]
}

maratonista3 = {
    "nombre" : "Ian Nigrola",
    "DNI" : "66666666",
    "maratones" : [{
        "nombre" : "Medio Maratón de Buenos Aires.",
        "anio" : 2017,
        "puesto" : 5,
        "tiempo" : 9474
    },
    {
        "nombre" : "Maratón Internacional de Buenos Aires.",
        "anio" : 2025,
        "puesto" : 4,
        "tiempo" : 9072
    }]
}
 """
# Implementación del inciso b.
""" 
maratonistas = [maratonista1,maratonista2,maratonista3] # Defino una lista de diccionarios.
def nombre_maratonista(maratonista): # Defino el encabezado de una función auxiliar.
    return maratonista["nombre"] # Devuelvo el nombre del maratonista.

maratonistas.sort(key=nombre_maratonista) # Ordeno la lista alfabeticamente.
print(maratonistas) # La muestro por pantalla.
 """
# Aclaración
""" 
El argumento key es el criterio de orden, o sea ordenar (alfabeticamente) por los nombres de los maratonistas.
 """
# Implementación del inciso c.
""" 
maratonistas = [maratonista1,maratonista2,maratonista3] # Defino una lista de diccionarios.
def maratones_cada_maratonista(maratones): # Defino el encabezado de una función auxiliar. maratones es una lista de diccionarios.
    return maratones["tiempo"] # Devuelvo el tiempo de cada maraton.

for maratonista in maratonistas: # Defino el encabezado del ciclo. Recorriendo a los maratonistas (una lista de diccionarios) maratonista (diccionario) a maratonista (diccionario).
    maratonista["maratones"].sort(key=maratones_cada_maratonista) # Ordeno la lista de diccionarios que está almacenada en la clave maratones de cada maratonista.

print(maratonistas) # Muestro por pantalla la lista de maratonistas.
 """
# Aclaración
""" 
El argumento key es el criterio de orden, o sea ordenar (ascendentemente) por los tiempos de las maratones.
 """
