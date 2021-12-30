import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'time': 4, 'ejection_fraction':20, 'serum_creatinine':1.9, 'age':75})

print(r.json())