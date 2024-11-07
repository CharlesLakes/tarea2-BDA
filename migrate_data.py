from pymongo import MongoClient
import json
import os

# Establecer la URI de conexión del Replica Set
uri = "mongodb://localhost:27017/?replicaSet=myReplicaSet&directConnection=true"

# Conectar a MongoDB
client = MongoClient(uri)

# Seleccionar la base de datos y la colección
db = client['Steam']
games_collection = db['Games']

# Eliminar la colección 'Games' si ya existe
games_collection.drop()

# Cargar datos del archivo games.json
dataset = {}
if os.path.exists('games.json'):
    with open('games.json', 'r', encoding='utf-8') as fin:
        text = fin.read()
        if len(text) > 0:
            dataset = json.loads(text)

# Total de juegos que se van a insertar
total_games = len(dataset)

# Contador de juegos insertados
inserted_count = 0

# Agregar cada juego a la colección "Games"
for app in dataset:
    game = dataset[app]  # Objeto del juego

    # Crear un documento con los datos, asegurándose de que las claves existan
    game_data = {}
    for key, value in game.items():
        if value is not None:  # Solo agregamos el campo si tiene un valor no nulo
            game_data[key] = value

    # Asegurarse de agregar el appID como campo principal
    game_data['appID'] = app

    # Insertar el documento en la colección "Games"
    games_collection.insert_one(game_data)

    # Actualizar el contador e imprimir el progreso
    inserted_count += 1
    print(f"Progreso: {inserted_count}/{total_games} juegos insertados.")

print("Datos insertados correctamente en la base de datos Steam.")
