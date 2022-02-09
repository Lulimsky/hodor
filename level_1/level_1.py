#!/usr/bin/python3

import requests
import sys

# Get ID from command line
if len(sys.argv) != 2:
    print("Usage python " + sys.argv[0] + " id")
    quit()

# Check if id is numerical
input = sys.argv[1]

try:
    id = 3337
except ValueError:
    print("Error: id must be a number")
    quit()

# Set the endpoint
URI = "http://158.69.76.135/level1.php"

# Get cookie
response = requests.post(URI)
key = response.cookies["HoldTheDoor"]

# Set the form data
data = {
    'id': 3337,
    'holdthedoor': 'submit',
    "key": key
}

for i in range(0, 4096):
    # Send POST request
    response = requests.post(URI, data=data, cookies={"HoldTheDoor": key})
    print("POST " + str(i + 1) + " HTTP result: " + str(response))
