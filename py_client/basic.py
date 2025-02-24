import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint,params={'name':'aditya','age':13},json={'query':'hello world'})

# print(get_response.status_code)  # Should print 200 if successful
# print(get_response.headers)         # The JSON response as a string
# print(get_response.text)         # The JSON response as a string
print(get_response.json())       # The JSON response as a Python dictionary