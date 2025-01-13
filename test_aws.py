""" Test Script for Cloud Deployment """
import requests

#url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
### I have changed the url, for data security and protection ,
### but the format should look like the one below:

url ='https://es4gq6qyt3.execute-api.us-east-1.amazonaws.com/prod/predict'

data = {"data" :{'Ia': -370.802352,
        "Ib":-526.475517, 
        "Ic": 897.381725,
        "Va":-0.042337,
        "Vb":0.019111, 
        "Vc":0.023226 }
}


result = requests.post(url ,json=data, timeout=30).json()
print(result)
