import pandas as pd
import csv
import requests
import cv2

#tomamos los archivo con los subfolios y lo pasamos a un diccionario
subfolios = csv.DictReader(open("subfolios.csv"))

#variables para almacenar los subfolios procesados 
subfolios_bien = []
subfolios_mal = []
#iterando para cada uno de los subfolios
for raw in subfolios:
    #extrayendo la url del código QR
    url_imagen = raw["QR"].split()
    url_imagen = url_imagen[1].split("(")
    url_imagen = url_imagen[1].split(")")
    url_imagen = url_imagen[0]
    
    #Dando nombre al código QR y descargando
    nombre_imagen = raw["Sub Folio de Pedido"] + ".jpg"
    imagen = requests.get(url_imagen).content
    with open(nombre_imagen, "wb") as handler:
        handler.write(imagen)
    
    #Empezando a analizar el QR para sacar su data
    img = cv2.imread(nombre_imagen)
    detector = cv2.QRCodeDetector()
    data, bbox, stight_code = detector.detectAndDecode(img)
    if data == raw["Sub Folio de Pedido"]:
        #subfolios_bien.append({"Subfolio": raw["Sub Folio de Pedido"]})
        print(data + " = " + raw["Sub Folio de Pedido"])
    else:
        #subfolios_mal.append({raw["Sub Folio de Pedido"]})
        print(data + " =! " + raw["Sub Folio de Pedido"])
    

"""dfSubBien = pd.DataFrame(data=subfolios_bien)
dfSubBien.to_csv('subfoliosBien.csv')

dfSubMal = pd.DataFrame(data=subfolios_mal)
dfSubMal.to_csv('subfoliosMal.csv')"""
    

