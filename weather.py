#Esse é um o Programa de Consulta da Previsão do tempo.

from PyQt5 import  uic,QtWidgets

# importando bilbiotecas
from PIL import ImageTk, Image
import requests
import datetime
import time

from datetime import datetime
import pytz
import pycountry_convert as pc


##### sobre dados ##
import json

################# cores ###############
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul


fundo_dia="#6cc4cc"
fundo_noite="#484f60"
fundo_tarde = "#bfb86d"

fundo = fundo_dia


################# Frames ####################

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_principal = Frame(janela, width=320, height=50,bg=co1, pady=0, padx=0, relief="flat",)
frame_principal.grid(row=1, column=0)


frame_quadros = Frame(janela, width=320, height=300,bg=fundo, pady=12, padx=0, relief="flat",)
frame_quadros.grid(row=2, column=0, sticky=NW)

style = ttk.Style(frame_principal)
style.theme_use("clam")


def info():
    #weather_key = '74db8d03761c1e007553ccbc6d73fe92'
    #cidade = e_local.get()
    #api_link = "https://api.openweathermap.org/data/2.5/weather?q="+cidade+"&appid="+ weather_key+"&lang=pt"

    #HTTP request
    r=requests.get(api_link)
    #convert the data in 'r' into dictionary
    data=r.json()

    # zona , pais, horas 
    pais_codigo = data['sys']['country']

    zona_fuso=pytz.country_timezones[pais_codigo]

    # --- pais ---
    pais = pytz.country_names[pais_codigo]

    # --- data ---
    zona = pytz.timezone(zona_fuso[0]) 
    zona_horas = datetime.now(zona)
    zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")

app=QtWidgets.QApplication([])
main=uic.loadUi("main.ui")
#main.pushButton.clicked.connect(funcao_principal)
#formulario.pushButton_2.clicked.connect(chama_segunda_tela)

main.show()
app.exec()