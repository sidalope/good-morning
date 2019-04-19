#!/usr/src/env python3

from send_text import Messenger
from dotenv import load_dotenv
from pathlib import Path
from os import getenv
from sys import argv
import requests

environment_path = Path('.') / '.env'
load_dotenv(dotenv_path=environment_path)
iris = getenv('IRIS')


def get_image(search_term):
    '''
    Return an image url from an image search for search_term

    TODO: get image url out. Google custom search api? ecosia api?
    '''

    ddg_search_url = '''https://duckduckgo.com/?q=zuckerberg&t=h_&iar=images
    &iax=images&ia=images'''
    result = requests.get(ddg_search_url)
    return result.text


if __name__ == '__main__':
    args_length = len(argv)
    # TODO: add recipient and url spec handling. Use flags?!1

    if args_length == 3:
        Messenger().send_message(argv[1], argv[2])
        #  TODO
        # image_url = get_image(argv[1])
        # sms_body = sms = f'''Good Morning! Today\'s exigent reason to
        #  ditch facebook: {image_url}'''
        # Messenger.send_text(iris, sms_body)
        print('Two arg call is under construction.')
    elif args_length == 1:
        # No args passed, default execution
        default_url = 'https://bit.ly/2ZbUn5P'
        sms_body = f'''Good Morning! All the reason you'll ever need \
to ditch facebook: {default_url}'''
        print(sms_body)
        # Messenger().send_message(iris, sms_body)
    else:
        print(f'You entered {args_length}.')
        print('I take either a search term, or no arguments.')
