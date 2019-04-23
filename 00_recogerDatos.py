'''
    File name: 00_recogerDatos.py
    Author: Juan Andres Corrochano
    Date created: 15/04/2019
    Date last modified: 23/04/2019
    Python Version: 3.6
    Description: En este script se realiza la peticion a la API de la EMT y se guarda el resultado en un fichero
'''

import requests
import json
import time
# Parameters needed to get the data
urlEMT = 'https://openbus.emtmadrid.es:9443/emt-proxy-server/last//geo/GetArriveStop.php'
idClient = 'WEB.SERV.juanan96lrs@gmail.com'
passKey = '0065F7B0-F675-4683-BF41-40B7560891B6'
idStop = '3537'

while True:
	time.sleep(1)
	req = requests.post(urlEMT, data = {'idClient' : idClient,
										'passKey': passKey,
										'idStop': idStop,
										'cultureInfo':'ES'})

	req.raise_for_status()
	with open("data.txt","a") as f:
		f.write(str(req.json())+'\n')
	print("Grabado")
    

