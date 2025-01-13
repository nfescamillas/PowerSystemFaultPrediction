""" Test Script for Local Deployment """
import requests

# Use the url below for running on local
# run the following code upon buidling docker
# docker run -it --rm -p 9696:9696  docker_image_name

url = 'http://localhost:9696/predict'

data ={ 'Ia': -370.802352,
        'Ib':-526.475517, 
        'Ic': 897.381725,
        'Va':-0.042337,
        'Vb':0.019111, 
        'Vc':0.023226 }


response = requests.post(url, json=data,timeout=30).json()
print(response)
