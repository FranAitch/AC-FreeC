## textMyself.py
# Defines the textmyself() funtion that texts a message
# passed to it as a string

from twilio.rest import TwilioRestClient

# Provide this with your twilio account info and your cell phone number (myCell)
accountSID = ''
authToken = ''
myTwilio = ''
myCell = ''

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=myTwilio, to=myCell)


