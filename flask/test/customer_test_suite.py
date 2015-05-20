'''
    Customer API testing suite
'''
__author__ = 'Jeyapriya'
import requests
from pprint import pprint

host = 'localhost'
port = 5000


url = 'http://%s:%s/'%(host,port)
url =  url+'%s'

#Start filters endpoint testing .

#Pass in a empty payload
login_endpoint_url = url%('customer/login')
payload = {}
response = requests.post(login_endpoint_url, json=payload)
assert response.status_code == 400
#print response.json()
assert response.json()['message'] == 'params cannot be empty'

#Pass in username
payload = {'username':'jp','password':'jp123'}
response = requests.post(login_endpoint_url, json=payload)
assert response.status_code == 200
assert response.json()['message'] == 'Login successful'

#Pass in user information
signup_endpoint_url = url%('customer/signup')
payload = {'username':'jptest1','password':'jp123','firstname':'JP','lastname':'GK','email':'jp@test.com'}
response = requests.post(signup_endpoint_url, json=payload)
assert response.status_code == 200
assert response.json()['message'] == 'Signup successful'

