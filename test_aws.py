import requests

#url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
url ='https://**********.execute-api.us-west-1.amazonaws.com/stage_name/resource_name'

data = {"data" :{'Ia': -370.802352,
        "Ib":-526.475517, 
        "Ic": 897.381725,
        "Va":-0.042337,
        "Vb":0.019111, 
        "Vc":0.023226 }
}


result = requests.post(url ,json=data, timeout=30).json()
print(result)