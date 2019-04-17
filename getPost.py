# Its needed: py -3 -m pip install requests (On Windows)
# Reference: https://code.tutsplus.com/es/tutorials/using-the-requests-module-in-python--cms-28204
import requests
import json
# Parameters needed to get the data
urlEMT = 'https://openbus.emtmadrid.es:9443/emt-proxy-server/last//geo/GetArriveStop.php'
idClient = 'WEB.SERV.juanan96lrs@gmail.com'
passKey = '0065F7B0-F675-4683-BF41-40B7560891B6'
idStop = '3537'

req = requests.post(urlEMT, data = {'idClient' : idClient,
                                    'passKey': passKey,
                                    'idStop': idStop,
                                    'cultureInfo':'ES'})

req.raise_for_status()
print ( len(req.json()['arrives']) ) # To know how many buses are near



