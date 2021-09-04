import requests

url = 'http://127.0.0.1:5000/results'
r = requests.post(url,json={'Postcode':6000, 'Bedrooms':2, 'Bathrooms':2})

print(r.json())