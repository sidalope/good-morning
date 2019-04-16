#!/usr/bin/env python3.7
from twilio.rest import Client
from sys import argv
from os import getenv
from dotenv import load_dotenv
from pathlib import Path

environment_path = Path('.') / '.env'
load_dotenv(dotenv_path=environment_path)

# Read Account SID and Auth Token (twilio.com/console)
account_sid = getenv('TWILIO_ACCOUNT_SID')
auth_token = getenv('TWILIO_AUTH_TOKEN')
sender = getenv('TWILIO_NUMBER')


class messenger:

    def send_message(self, recipient, body):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                to=recipient,
                from_=sender,
                body=body)

        return message.sid


if __name__ == '__main__':
    # Takes phone number as first argument and sms body as second
    if len(argv) == 3:
        recipient = argv[1]
        body = argv[2]
        # print(f'from: {sender} to: {receiver} message: {body}')

        messenger().send_message(recipient, body)
    else:
        print(f'You passed in {len(argv)} arguments.')
        print('send_text takes 2 arguments: a recipient and a message body.')
