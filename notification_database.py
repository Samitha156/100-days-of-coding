from twilio.rest import Client

TWILIO_SID = "AC22a576bf0fa38cb70e45832024b35bfc"
TWILIO_AUTH_TOKEN = "c9b9b5bfebdc300f19fa9b5a8777f62d"
TWILIO_VIRTUAL_NUMBER = "+19286156986"
TWILIO_VERIFIED_NUMBER = "+13303226254"


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        # prints if successfully sent.
        print(message.sid)
