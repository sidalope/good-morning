#!/usr/bin/env python3
from sys import argv
from os import getenv
import logging
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


class Messenger:
    account_sid = getenv('TWILIO_ACCOUNT_SID')
    auth_token = getenv('TWILIO_AUTH_TOKEN')
    sender = getenv('TWILIO_NUMBER')

    test_account_sid = getenv('TEST_ACCOUNT_SID')
    test_auth_token = getenv('TEST_AUTH_TOKEN')
    test_sender = getenv('TEST_NUMBER')
    test_recipient = getenv('TEST_RECIPIENT')

    client = Client(test_account_sid, test_auth_token)

    # Define logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('./log.txt')
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    client.http_client.logger.setLevel(logging.INFO)


    def send_message(self, body, recipient=test_recipient):
        '''
        Send an sms "body" to "recipient", and log the sid on a
        successful send

        Returns:
        {str} : the message delivery status
        '''
        # print(self.test_sender)
        message = self.client.messages.create(
                body = body,
                from_ = self.test_sender,
                to = recipient)

        return message.status


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
        response = Messenger().send_message(body, recipient)
        print(response.sid)
    elif len(argv) == 2:
        body = argv[1]
        response = Messenger().send_message(body)
        print(response)
    else:
        print(f'You passed in {len(argv) - 1} arguments.')
        print('send_text takes 2 arguments: a recipient and a message body.')
