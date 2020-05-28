import requests
from data_in import data1

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data1}

r = requests.get(URL,headers=headers, json=data)

r.json()