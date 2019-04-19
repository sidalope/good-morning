#!/usr/bin/env python3
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


class Messenger:

    def send_message(self, recipient, body):
        '''
        Send an sms "body" to "recipient", and log the sid on a
        successful send

        Returns:
        {str} : the message sid
        '''
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                to=recipient,
                from_=sender,
                body=body)

        self.log_sms(message.sid, recipient, body)
        return message.sid


    def log_sms(self, sid, recipient, body):
        '''
        Log an sms by printing to stdout

        TODO: Append to a file. Add file path in args for github.
        '''
        print(f'sid: {sid}')
        print(f'Sent to: {recipient}')
        print(f'Body: {body}\r\n')


if __name__ == '__main__':
    # Takes phone number as first argument and sms body as second
    if len(argv) == 3:
        recipient = argv[1]
        body = argv[2]

        Messenger().send_message(recipient, body)
    else:
        print(f'You passed in {len(argv)} arguments.')
        print('send_text takes 2 arguments: a recipient and a message body.')
