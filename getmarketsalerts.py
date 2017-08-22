import requests
import json
import smtplib

try:
    with open('markets.json', 'r') as current_markets:
        before = json.loads(current_markets.read())
except IOError:
    before = requests.get('https://bittrex.com/api/v1.1/public/getmarkets').json()
    with open('markets.json', 'w') as current_markets:
        current_markets.write(json.dumps(before))
    print("First run... Getting initial market data.")

after = requests.get('https://bittrex.com/api/v1.1/public/getmarkets').json()

before_set = set([market['MarketName'] for market in  before['result']])
after_set = set([market['MarketName'] for market in  after['result']])

new_set = after_set - before_set

if new_set:
    with open('markets.json', 'w') as current_markets:
        current_markets.write(json.dumps(after))
    print('Bittrex has added the following pairs:')
    for pair in new_set:
        new_list = list([''.join((item) for item in pair)])
        print(new_list)

    sender = 'example@example.com'
    receivers = ['example@example.com']

    message = """
    Bittrex has added the following pairs:\n + new_list + \n
    Get 'em while they're juicy!
    """

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.gmail.com:465')
        smtpObj.login('example@example.com','password')
        smtpObj.sendmail(sender, receivers, message)         
        print("\nSuccessfully sent email")
    except SMTPException:
       print("\nError: unable to send email")
