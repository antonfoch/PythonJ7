import json

f = open('D-POO-300_07_nobelLaureates.json')

data = json.load(f)


data_type = type(data)
print(data_type)

cinq_premiers = data['laureates']
print(json.dumps(cinq_premiers[:5], indent=2))

