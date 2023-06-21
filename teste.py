import requests
import datetime
import json

chave = 'c68a489eac0d7c85d0d72141a18c121c'
api_link = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=c68a489eac0d7c85d0d72141a18c121c'

r = requests.get(api_link)

dados = r.json()

print(dados)