import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

#crea un DataFrame de ejemplo con las califiicaciones de los usarios para peliculas
data = {
    'Usuario A':[5,4,0,0,0],
    'Usuario B':[0,5,4,0,0],
    'Usuario C':[0,0,5,4,0],
    'Usuario D':[0,0,0,5,4]
}

df= pd.DataFrame(data, index=['Pelicula 1','Pelicula 2','Pelicula 3','Pelicula 4','Pelicula 5'])

#Calcular la similitud de coseno entre peliculas

similarity_matrix= cosine_similarity(df.T)

#Pelicula Objetivo
pelicula_actual= 'Pelicula 1'

#Encontrar peliculas similares a la pelicula actual 
peliculas_similares =list(df.index[similarity_matrix[df.columns.get_loc(pelicula_actual)].argsort()[::-1]])

#Recoemndar peliculas similares a la pelicula actual
recomendaciones=df.loc[peliculas_similares[1:]].idxmax()
print(f"Pelicula similar a {pelicula_actual}: {peliculas_similares[1]}")
print(f"Recomendaciones basadas en {pelicula_actual}:{recomendaciones.tolist()}")