
"""
This module imports the 'requests' library, which allows making HTTP requests in Python.
"""
import requests
URL = "http://127.0.0.1:8000/stuinfo/"

r= requests.get(url = URL)

data= r.json()
print(data)