import json

with open('cumpleaños.json') as json_file:
    json_decoded = json.load(json_file)

diccionario = {}
for i in range(1,13):
    mes = "0"+str(i) if i <10 else str(i)
    for j in range(1,32):
        dia = "0"+str(j) if j <10 else str(j)
        diccionario[dia+"/"+mes] = []   

json_decoded = diccionario

with open('cumpleaños.json', 'w') as data:
    json.dump(json_decoded, data)