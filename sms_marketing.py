from twilio.rest import Client
account_sid = "Your_Accoutn_Sid"
auth_token  = "Your_Auth_Token"
client = Client(account_sid, auth_token)
  
message = open("message.txt","r").read()
contact = open("contact.txt", "r").read().split(',')
for x in contact:
    message = client.messages.create(
        to=x, 
        from_="+15028920419", #use your own Number From Twilio
        body=message)

