import json
import redis

# Connexion à Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Ouvrir et lire le fichier JSON
with open('mon_fichier.json', 'r') as f:
    data = json.load(f)

# Ingestion des données dans Redis
for key, value in data.items():
    r.set(key, json.dumps(value))
