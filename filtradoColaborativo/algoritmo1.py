import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

#Crea un DataFrame de ejemplo con las preferencias en peliculas 
data = {
    'Usuario A':[5,4,0,0,3],
    'Usuario B':[0,5,4,0,0],
    'Usuario C':[0,0,5,4,0],
    'Usuario D':[4,0,0,5,4]
}

df = pd.DataFrame(data)

#Calcular la similitud de coseno entre usuarios
similarity_matrix = cosine_similarity(df)

#Usuario Objetivo
usuario_actual= 'Usuario A' 

#Encontrar los usuarios mas similares al usuario actual
similar_users= list(df.columns[df.loc[usuario_actual].values.argsort()[::-1]])

#Recomendar peliculas basadas en las preferencias de usuarios similares

recomendaciones= df[similar_users[1:]].max(axis=1)
recomendaciones= recomendaciones[recomendaciones>0].index.tolist()

print(f"Usuarios similares a {usuario_actual}: {similar_users[1:]}")
print(f"Recomendaciones para {usuario_actual}: {recomendaciones}")