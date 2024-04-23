# first you need to create a twilio account. and verify the number
# next is install the twilio using pip install twilio
from twilio.rest import Client

account_sid = 'AC1199117d446fa6d714da9b3c48b7006d'
auth_token = 'f78731e9680769207591e3cbc643e8e2'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12512204652',
    body='I CANT BELIEVE THIS WORKS',
    to='+639761310785'
)

print(message.sid)
