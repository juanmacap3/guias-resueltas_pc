""" 
===============================
Si es la primera vez que abrís uno de estos archivos te recomiendo mirar el readme.
===============================
 """

import matplotlib.pyplot as plt
import pandas as pd
# Enunciado
""" 
Graficar la función . Pueden usar de ejemplo el apunte donde está graficada la función𝑓(𝑥) = 𝑥³
.𝑓(𝑥) = 𝑥²
 """
# Implementación
""" 
x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10] # Defino el eje x.
y = [-1000, -729, -512, -343, -216, -125, -64, -27, -8,-1,0,1,8,27,64,125,216,343,512,729,1000] # Defino el eje y.

plt.plot(x,y) # Genero el plot con ambos ejes.
plt.show() # Muestro el plot.
 """
# Enunciado
""" 
La siguiente lista contiene las temperaturas en celsius a lo largo del día medidas cada 30 minutos:
[15, 16, 16, 17, 16, 15, 14, 14, 14, 15, 16, 15, 15, 16, 15, 14, 13,
12, 12, 12, 12, 13, 14, 15, 16, 17, 18, 18, 18, 18, 18, 18, 18, 17,
17, 16, 16, 16, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
El primer elemento corresponde a la temperatura a las 00:00 y la última a las 23:30. Realizar un gráfico
que tenga en el eje X la hora y en el eje Y la temperatura. Darle un título y anotar que representa cada
eje.
 """
# Implementación
""" 
# Defino los ejes.
y = [15, 16, 16, 17, 16, 15, 14, 14, 14, 15, 16, 15, 15, 16, 15, 14, 13, 12, 12, 12, 12, 13, 14, 15, 16, 17, 18, 18, 18, 18, 18, 18, 18, 17, 17, 16, 16, 16, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
x = ["00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]

plt.plot(x, y) # Genero el plot con los ejes.
# Defino las etiquetas para los ejes y el título del plot.
plt.xlabel("Horas")
plt.ylabel("Temperatura")
plt.title("Temperaturas durante el día.")
plt.show() # Muestro el plot.
 """
# Enunciado
""" 
Usando el set de datos de películas de la guía de ejercicios de pandas. Hacer un gráfico de barras que
muestre la cantidad de películas de cada género.
 """
# Implementación
"""
# Defino el set.
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

generos = df.groupby("género")["nombre"].count() # Ordeno por genero y cuento la cantidad de películas que hay.

# Defino dos listas vacías
x = []
y = []

# Defino el encabezado del ciclo. Recorro la secuencia que tiene por elementos tuplas cuyo primer elemento es el genero y el segundo la cantidad.
for genero in generos.items():
    x.append(genero[0]) # Guardo en esta lista los géneros que hay.
    y.append(genero[1]) # Guardo en esta lista la cantida de películas que hay.

plt.bar(x,y) # Genero el gráfico de barras con los ejes.
plt.show() # Muestro el gráfico.
 """
# Enunciado
""" 
Usando el set de datos de películas de la guía de ejercicios de pandas. Hacer un gráfico de torta que
muestre la proporción de películas vistas y no vistas.
 """
# Implementación
""" 
# Defino el set.
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
# Defino una variable para contar las peliculas no vistas.
cant_peliculas_no_vistas = 0


for puntaje in peliculas["puntaje"]: # Defino el encabezado del ciclo. Recorriendo la lista de puntajes, puntaje por puntaje.
    if puntaje is None: # Verifico si el puntaje está vacío.
        cant_peliculas_no_vistas += 1 # En ese caso le sumo uno al contador.


cant_peliculas_vistas = len(peliculas["puntaje"]) - cant_peliculas_no_vistas # Calculo las películas vistas.
porciones = [cant_peliculas_no_vistas, cant_peliculas_vistas] # Guardo en una lista la cantidad de películas vistas y las no vistas.
etiquetas = ["Películas no vistas", "Películas vistas"] # Guardo en otra lista las etiquetas que quiero mostrar.

plt.pie(porciones, labels=etiquetas, autopct='%1.1f%%') # Genero el gráfico de torta.
plt.show() # Muestro el gráfico.
 """
# Enunciado
""" 
Dado el siguiente set de datos misterioso que contiene una serie de puntos con formato (x,y):
[(0.3, 0.46),
(0.3286, 0.4176),
(0.3571, 0.3816),
(0.3857, 0.3522),
(0.4143, 0.3294),
(0.4429, 0.3131),
(0.4714, 0.3033),
(0.5, 0.3),
(0.5286, 0.3033),
(0.5571, 0.3131),
(0.5857, 0.3294),
(0.6143, 0.3522),
(0.6429, 0.3816),
(0.6714, 0.4176),
(0.7, 0.46),
(0.35, 0.63),
(0.65, 0.63),
(0.5, 0.5)]
Hacer un gráfico de dispersión que muestre todos los puntos.
 """
# Implementación
""" 
# Defino la lista de puntos misteriosos.
coordenadas = [
    (0.3, 0.46), (0.3286, 0.4176), (0.3571, 0.3816),
    (0.3857, 0.3522), (0.4143, 0.3294), (0.4429, 0.3131),
    (0.4714, 0.3033), (0.5, 0.3), (0.5286, 0.3033),
    (0.5571, 0.3131), (0.5857, 0.3294), (0.6143, 0.3522),
    (0.6429, 0.3816), (0.6714, 0.4176), (0.7, 0.46),
    (0.35, 0.63), (0.65, 0.63), (0.5, 0.5)]

# Defino dos listas vacías
x = []
y = []

# Recorro la lista de puntos y agrego las coordenadas en cada lista.
for coord in coordenadas:
    x.append(coord[0]) # Agrego el primer elemento en la lista de las coordenadas en x.
    y.append(coord[1]) # Agrego el segundo elemento en la lista de las coordenadas en y.

plt.scatter(x,y) # Genero el gráfico de dispersión con los ejes generados anteriormente.
plt.show() # Muestro el gráfico.
 """
