from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import requests
import sys
import httplib2

print("insert URL: ")
req=input()

try:
    response = requests.get(req, timeout=10)
    print(response.status_code)
except:
    sys.exit()

