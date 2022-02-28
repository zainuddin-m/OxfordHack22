import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "" #add your token here
auth_token = "" #add your token between the quotation marks
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         messaging_service_sid='', #add your messaging service token here
         body='get off league youre a tincan elo player with 0% winrate, get a life', #add your message here
         to='' #add the number you want the sms to be sent to here
     )

print(message.sid)
