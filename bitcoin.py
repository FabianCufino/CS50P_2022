import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    qty = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")

try:
   r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
   #print (r,dir(r))
   json1 = r.json()
   #print(json1)
   #print(type(json1))
   value = float(json1["bpi"]["USD"]["rate_float"])
   #print (json2)
   print(f"${value*qty:,.4f}")
except requests.RequestException:
    sys.exit("Error with api")
