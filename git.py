import json
import requests
import pandas as pd 
from googleapiclient.discovery import build

"""credencial API"""
key_api = "AIzaSyCB6OPDrOftLyG1lVbDYDgyw1i4XEdOwys"

youtube = build('youtube','v3', developerKey=key_api)

rd = "Reydama"
padel = "@Worldpadeltour"
requests = youtube.channels().list(part='statistics', forUsername = padel)

response = requests.execute()
#print(response)

"""Obtener comentarios del video"""
# Extraer el ID del video de la URL
url = "https://www.youtube.com/watch?v=6wQx52edorY"
video_id = url.split('=')[1]

# Llamada a la API para obtener los comentarios
comments = youtube.commentThreads().list(
    part='snippet',
    videoId=video_id,
    textFormat='plainText'
).execute()

# Recorrer los comentarios obtenidos e imprimir su contenido
msj = []
for comment in comments['items']:
    text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
    msj.append(text)
    pass

def proc(msj):
    stok = ""