#Register in some API to create REST, and generate [Auth_Tokens]
from twilio.rest import Client

account_sid = 'Enter the sid'
auth_token = 'Grab the Auth_Token from the RestAPI'
client = Client(account_sid, auth_token)


message = client.messages.create(from_='+919787xxxxxx',
                                 body= 'Hello! SMS sent via python! Wohoo',
                                 to='+919876xxxxxx'

)

print(message.sid)
