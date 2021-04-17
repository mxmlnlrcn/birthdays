import json

def add():
    print('Enter the full name')
    nombre = input()
    print('Enter the phone number')

    numero= input()
    n = [i for i in str(numero)]
    check = True
    while check:
        if n[0] == '+' :
            check = False
        else:
            print('Enter a valid phone number ej: +XXXXXXXXXXX')
            numero= input()
            n = [i for i in str(numero)]

    print('Enter the nickname')
    apodo = input()
    print('Enter the clossenes (family, friend, other)')
    cercania = input()
    check = True
    while check:
        if cercania in ['family', 'friend', 'other']:
            check = False
        else:
            print('Enter a valid type of clossenes (family, friend, other)')
            cercania = input()
    print('Enter the birth date ej: DD/MM')
    fecha = input()
    check = True
    while check:
        if (fecha[2] == "/") & (len(fecha) == 5):
            check = False
        else:
            print('Enter a valid date ej: DD/MM')
            fecha = input()
    
    with open('birthdays.json') as json_file:
        json_decoded = json.load(json_file)

    json_decoded[fecha].append({'nombre' : nombre, 'numero' : numero, 'apodo': apodo, 'cercania': cercania})

    with open('birthdays.json', 'w') as data:
        json.dump(json_decoded, data)

def eliminar():
    print('What number do you whant to delete?')
    numero = input()
    with open('birthdays.json') as json_file:
        json_decoded = json.load(json_file)
    
    check = True
    for i in json_decoded:
        cant = len(json_decoded[i])
        if cant != 0:
            for j in range(cant):
                if json_decoded[i][j]['numero'] == numero:
                    del json_decoded[i][j]
                    print('deleted')
                    check = False
                    break

    if check:
        print('Phone number not found')
    else:
        with open('birthdays.json', 'w') as data:
            json.dump(json_decoded, data)

def ver():
    print('What number do you want to see?')
    numero = input()
    with open('birthdays.json') as json_file:
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
        print('Phone number not found')


while True:
    print('What do you want to do? ( Add (A) , Delete (D) , See (S) ,  Quit (Q) )')
    opcion = input()
    check = True
    while check:
        if opcion in ['A' , 'D'  , 'a' , 'D' , 'Q', 'Q' , 'S' , 's'] :
            check = False
        else:
            print('Please, enter a valid optiona ( Add (A) , Delete (D) , See (S) ,  Quit (Q) )')
            opcion = input()

    if opcion in ['A' , 'a']:
        add()
    elif opcion in ['D' , 'd']:
        eliminar()
    elif opcion in ['s' , 'S']:
        ver()
    elif opcion in ['Q', 'q']:
        break

