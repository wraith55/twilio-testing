# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+15053571348',
                        from_='+15053571348'
                    )

print(call.sid)
