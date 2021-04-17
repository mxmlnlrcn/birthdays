import json

# with open('cumpleaños2.json') as json_file:
#     json_decoded = json.load(json_file)


def add():
    print('Ingrese el nombre completo')
    nombre = input()
    print('Ingrese el numero de esta persona')

    numero= input()
    n = [i for i in str(numero)]
    check = True
    while check:
        if n[0] == '+' :
            check = False
        else:
            print('Ingrese numero de nuevo ej: +569XXXXXXXX')
            numero= input()
            n = [i for i in str(numero)]

    print('Ingrese el apodo de esta persona')
    apodo = input()
    print('Ingrese el tipo de cercania (familiar, amigo, otro)')
    cercania = input()
    check = True
    while check:
        if cercania in ['familiar' , 'amigo' , 'otro']:
            check = False
        else:
            print('Ingrese tipo de cercania valido: (familiar, amigo, otro)')
            cercania = input()
    print('Ingrese fecha de cumpleaños ej: DD/MM')
    fecha = input()
    check = True
    while check:
        if (fecha[2] == "/") & (len(fecha) == 5):
            check = False
        else:
            print('Ingrese una fecha valida ej: DD/MM')
            fecha = input()
    
    with open('cumpleaños.json') as json_file:
        json_decoded = json.load(json_file)

    json_decoded[fecha].append({'nombre' : nombre, 'numero' : numero, 'apodo': apodo, 'cercania': cercania})

    with open('cumpleaños.json', 'w') as data:
        json.dump(json_decoded, data)

def eliminar():
    print('¿Que numero desea eliminar?')
    numero = input()
    with open('cumpleaños.json') as json_file:
        json_decoded = json.load(json_file)
    
    check = True
    for i in json_decoded:
        cant = len(json_decoded[i])
        if cant != 0:
            for j in range(cant):
                if json_decoded[i][j]['numero'] == numero:
                    del json_decoded[i][j]
                    check = False
                    break

    if check:
        print('No se ha encontrado el numero de telefono')
    else:
        with open('cumpleaños.json', 'w') as data:
            json.dump(json_decoded, data)

def ver():
    print('¿Que numero desea ver?')
    numero = input()
    with open('cumpleaños.json') as json_file:
        json_decoded = json.load(json_file)
    
    check = True
    for i in json_decoded:
        cant = len(json_decoded[i])
        if cant != 0:
            for j in range(cant):
                if json_decoded[i][j]['numero'] == numero:
                    print(json_decoded[i][j])
                    check = False
                    break

    if check:
        print('No se ha encontrado el numero de telefono')


while True:
    print('¿Que desea hacer? ( Agregar (A) , Eliminar (E) , Ver (V) ,  Salir (S))')
    opcion = input()
    check = True
    while check:
        if opcion in ['A' , 'E'  , 'a' , 'e' , 'S', 's' , 'V' , 'v'] :
            check = False
        else:
            print('Ingrese opcion valida ( Agregar (A) , Eliminar (E) , Ver (V) , Salir (S))')
            opcion = input()

    if opcion in ['A' , 'a']:
        add()
    elif opcion in ['E' , 'e']:
        eliminar()
    elif opcion in ['V' , 'v']:
        ver()
    elif opcion in ['S', 's']:
        break

