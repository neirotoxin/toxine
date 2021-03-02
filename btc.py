from telethon import TelegramClient, events, sync
from random import choice
import time

api_id = 3248176
api_hash = 'd264b02b8be917f0a370edc3b3544748'

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.

client = TelegramClient('session_name', api_id, api_hash)
client.start()

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = 300
length = 32

for n in range(number):
    password = ''
    for i in range(length):
        password += choice(chars)
    client.send_message('BTC_CHANGE_BOT', f'/start c_{password}')
    time.sleep(2)