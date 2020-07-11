# -*- coding: utf-8 -*-
import amanobot
from amanobot.loop import MessageLoop
from time import sleep


def recebendo(msg):
    with open('bot_pack/centralMessages.txt', 'r', encoding='utf-8') as file:
       print(file.readline([1]))
    # bot.download_file(msg['voice']['file_id'], "D:\usuario\Documents\oice_hall")
    # bot.download_file(msg['voice']['file_id'], r'C:\hall')
    # bot.download_file(msg['voice']['file_id'], r'D:\usuario\Documents\oice_hall.mp3')
    #bot.download_file(msg['voice']['file_id'], r'D:\usuario\Documents\oice_hall.mp3')
    

# Coloca seu token do seu bot aqui em baixo
TOKEN = "870167339:AAEXvrPJf8NR9GWoOTWUvw-gdeGPy7kDkDE"
bot = amanobot.Bot(TOKEN)
MessageLoop(bot, {'chat': recebendo}).run_as_thread()

while True:
    sleep(5)
