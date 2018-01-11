import json

with open('superheroes.json') as f:
    data = json.load(f)

print data