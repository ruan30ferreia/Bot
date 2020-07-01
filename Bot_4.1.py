# -*- coding: utf-8 -*-
import amanobot
from amanobot.loop import MessageLoop
from time import sleep


def recebendo(msg):
    print(msg)
    #bot.download_file(msg['voice']['file_id'], "D:\usuario\Documents\oice_hall")
    # bot.download_file(msg['voice']['file_id'], r'C:\hall')
    # bot.download_file(msg['voice']['file_id'], r'D:\usuario\Documents\oice_hall.mp3')
    bot.download_file(msg['voice']['file_id'], r'D:\usuario\Documents\oice_hall.ogg')


# Coloca seu token do seu bot aqui em baixo
TOKEN = "AQUI"
bot = amanobot.Bot(TOKEN)
MessageLoop(bot, {'chat': recebendo}).run_as_thread()

while True:
    sleep(5)
