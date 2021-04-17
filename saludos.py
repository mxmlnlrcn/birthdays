from pywhatkit import sendwhatmsg 
import datetime
from numpy import random , sort
import numpy
import json

fecha = datetime.datetime.now().strftime("%d/%m")
cumpleaños = json.load(open('cumpleaños.json'))

while True:
    if fecha == ahora: # si la fecha sigue siendo la misma
        ahora = datetime.datetime.now().strftime("%d/%m")
    else: # si la fecha cambio
        fecha = ahora
        now = datetime.datetime.now()
        if len(cumpleaños[fecha]) != 0:
            cumpleañeros = len(cumpleaños[fecha])
            hora = sort(random.randint(max(int(now.hour+1) , 10) , 15, size = (cumpleañeros))).astype(str)
            minutos = sort(random.randint(0, 59, size = (cumpleañeros))).astype(str)
            for i in range(cumpleañeros):
                numero = cumpleaños[fecha][i]['telefono']
                apodo = cumpleaños[fecha][i]['apodo']
                if cumpleaños[fecha][i]['cercania'] == 'amigo':
                    mensaje = "What's uuup "+apodo+" Happy birthday!!!!, have a wonderfull day"   
                else:
                    mensaje = "Happy birthday "+apodo+", Have a nice day"

                sendwhatmsg(numero, mensaje , hora[i],minutos[i])



