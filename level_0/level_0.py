#!/usr/bin/python3

import requests
import sys
# import from bs4 import BeautifulSoup

# Get ID from command line
if len(sys.argv) != 2:
    print("Usage python " + sys.argv[0] + " id")
    quit()

# Check if id is numerical
input = sys.argv[1]

try:
    id = int(input)
except ValueError:
    print("Error: id must be a number")
    quit()

# Set the endpoint
URI = "http://158.69.76.135/level0.php"

# Set the form data
data = {
    'id': (None, id),
    'holdthedoor': (None, 'enviar'),
}

for i in range(0, 1024):
    # Send POST request
    response = requests.post(URI, data=data)

    # Print progress
    print("POST " + str(i + 1) + " HTTP result: " + str(response))
