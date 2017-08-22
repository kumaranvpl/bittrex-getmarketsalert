import requests
import json

try:
    with open('markets.json', 'r') as current_markets:
        before = json.loads(current_markets.read())
except IOError:
    before = requests.get('https://bittrex.com/api/v1.1/public/getmarkets').json()
    with open('markets.json', 'w') as current_markets:
        current_markets.write(json.dumps(before))

after = requests.get('https://bittrex.com/api/v1.1/public/getmarkets').json()

before_set = set([market['MarketName'] for market in  before['result']])
after_set = set([market['MarketName'] for market in  after['result']])

new_set = after_set - before_set

if new_set:
    with open('markets.json', 'w') as current_markets:
        current_markets.write(json.dumps(after))
    print('Bittrex has added the following pairs:')
    print(new_set)    
# List comprehension

# add email scipt here

print ("\n...results sent via email.")
