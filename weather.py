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

app=QtWidgets.QApplication([])
main=uic.loadUi("main.ui")
#main.pushButton.clicked.connect(funcao_principal)
#formulario.pushButton_2.clicked.connect(chama_segunda_tela)

main.show()
app.exec()