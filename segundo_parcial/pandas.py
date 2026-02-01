""" 
===============================
Si es la primera vez que abrís uno de estos archivos te recomiendo mirar el readme.
===============================
 """

import pandas as pd

peliculas = {'nombre': ['Titanic', 'Kil Bill', 'Matrix', 'El padrino', 'Avatar',
                        'Casablanca', 'El exorcista',  'Soy leyenda',
                        'El club de la pelea', 'Mujercitas'],
            'director': ['James Cameron', 'Quentin Tarantino', 'Hermanas Wachowski',
                        'Francis Ford Coppola', 'James Cameron', 'Michael Curtiz',
                        'William Friedkin', 'Francis Lawrence','David Fincher',
                        'Greta Gerwig'],
            'año': [1997, 2003, 1999, 1972, 2009, 1942, 1973, 2007, 1999, 2019],
            'género': ['romance', 'acción', 'ciencia ficción', 'drama', 'ciencia ficción', 'drama', 'terror',
                        'ciencia ficción', 'drama', 'drama'],
            'puntaje': [8.6, None, 6.9, 7.5, 9.1, 6.0, None, None, 9.4, 8.0]}

df = pd.DataFrame(peliculas)

# Enunciado
""" 
Mostrar sólo los nombres de las primeras 3 películas del DataFrame.
 """
# Implementación
""" 
print(df.head(3))
 """
# Enunciado
""" 
Mostrar sólo el director y el género de todas las películas.
 """
# Implementación
""" 
print(df[["director", "género"]])
 """
# Enunciado
""" 
Mostrar las películas que sean de drama.
 """
# Implementación
""" 
print(df[df["género"] == "drama"])
 """
# Enunciado
""" 
¿Qué cantidad de películas hay de cada género?
 """
# Implementación
""" 
generos = df.groupby("género")["nombre"].count() # Ordeno por genero y cuento la cantidad de películas que hay.
print(generos)
 """
# Enunciado
""" 
Mostrar las películas que tengan puntaje entre 6 y 8 y cuyo año de estreno sea anterior a los 2000.
 """
# Implementación
""" 
print(df[df["puntaje"].between(6,8) & df["año"] < 2000])
 """
# Enunciado
""" 
Mostrar las películas que no hayan sido puntuadas (que el puntaje tenga un valor nulo).
 """
# Implementación
""" 
print(df[df["puntaje"].isnull()])
 """
# Enunciado
""" 
Calcular el promedio del puntaje de todas las películas.
 """
# Implementación
""" 
print(df["puntaje"].mean())
 """
# Enunciado
""" 
Ordenar las películas en orden alfabético descendente.
 """
# Implementación
""" 
print(df.sort_values(by=["nombre"], ascending=[False]))
 """
# Enunciado
""" 
Mostrar las 3 películas más antiguas.
 """
# Implementación
""" 
orden_mas_antigua = df.sort_values(by=["año"], ascending=[True])
print(orden_mas_antigua.head(3))
 """
# Enunciado
""" 
Mostrar sólo el nombre y el año de las 3 películas más nuevas.
 """
# Implementación
""" 
orden_mas_actuales = df.sort_values(by=["año"], ascending=[False])
print(orden_mas_actuales[["nombre", "año"]].head(3))
 """
# Enunciado
""" 
Agregar una columna que indique si la película fue vista, o no. Una película fue vista cuando tiene
puntaje no nulo
 """
# Implementación
""" 
vista = [] # Defino una lista vacía.

for puntaje in peliculas["puntaje"]: # Defino el encabezado del ciclo. Recorriendo los puntajes de la tabla, puntaje por puntaje.
    if puntaje is None: # Verifico si el puntaje está vacío.
        vista.append(False) # En ese caso agrego a la lista vacía que definí antes el valor de verdad falso.
    else:
        vista.append(True) # En caso contrario agrego el valor de verdad verdadero.

df["vista"] = vista # Agrego la columna vista y le doy de valor la lista.
 """