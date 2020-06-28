# -*- coding: utf-8 -*-
import random

import amanobot
import emojis
from amanobot.loop import MessageLoop

from bot_pack.CentraLibrary import *
from bot_pack.buttonFunction import *
from bot_pack.messageHandling import ABC
from bot_pack.textModifiers import *
from bot_pack.timeNow import *


def soma(estrutura, name):
    return estrutura.replace("$", name)


def soma_hora(res12):
    return res12.replace("*", hour())


def recebendo(msg):
    chatID = msg['chat']['id']
    a = msg['text'] if ('text' in msg) else ''
    conta = a.split()
    letras_mens = list(a)
    aviso_x = emojis.encode(":x:")
    risadinha = emojis.encode(":joy:")

    if 'new_chat_member' in msg:
        receiving_new_users(msg, bot)

    elif len(a) > 0:
        limpesa = ABC(msg['text'])
        if limpesa == 'hall menu' or limpesa == 'menu hall':
            bot.sendMessage(chatID, "***OPÇÕES DO MENU CLIQUE***", reply_markup=botao2())

        elif limpesa == 'hall2':
            bot.sendMessage(chatID, "Todos os usuarios que não tiverem foto seram BANIDOS! Por "
                                    "favor colocar foto de perfil!")

        elif limpesa == 'hall que dia e hoje' or limpesa == 'que dia e hoje hall':
            bot.sendMessage(chatID, f"Hoje é dia {dat()}")

        elif conta[0] == '+':
            conta.pop(0)
            men_s = ' '.join(conta)
            bot.sendMessage(-1001140402839, text=men_s)

        elif limpesa == 'hall aviso grupo':
            bot.sendMessage(-1001140402839, "Todos os usuarios que não tiverem foto seram BANIDOS!"
                                            " Por favor colocar foto de perfil!")
            sleep(0.5)
            bot.sendMessage(-1001140402839, f"{aviso_x * 4}")
            bot.sendMessage(-1001140402839, "Quem não souber colocar foto no perfil, olhem o video abaixo!")
            bot.sendMessage(-1001140402839, "https://www.youtube.com/watch?v=gjroA6z6T7U&t=211s")
            bot.sendMessage(-1001140402839, "Ultimo aviso!")
            sleep(0.5)
            bot.sendMessage(-1001140402839, f"{aviso_x * 4}")

        elif letras_mens.count('k') > 6:
            bot.sendMessage(chatID, f"Qual a graça, {msg['from']['first_name']} ?")
            bot.sendMessage(chatID, text=risadinha)

        elif letras_mens.count('?') > 4:
            bot.sendMessage(chatID, f"Qual a duvida,posso ajudar {msg['from']['first_name']}?")

        else:
            with open('centralMessages.txt', 'r', encoding='utf-8') as file:
                for frase_pv in file:
                    frase_pv = frase_pv.replace('\n', '')
                    estrutura = frase_pv.split(':')
                    if len(estrutura) == 2:
                        resposta_ao_telegram = estrutura[1]
                        if limpesa == estrutura[1]:
                            bot.sendMessage(chatID, resposta_ao_telegram)
                            return

                    elif len(estrutura) >= 3:
                        if estrutura[0] and estrutura[1] in globals():
                            if limpesa == estrutura[2]:
                                resposta_final = random.choice(estrutura[3::])
                                if '$' or '*' in resposta_final:
                                    name = msg['from']['first_name']
                                    resposta_ao_telegram = globals()[estrutura[0]](resposta_final, name)
                                    resposta_ao_telegram = globals()[estrutura[1]](resposta_ao_telegram)
                                    bot.sendMessage(chatID, resposta_ao_telegram)
                                    return

                        elif estrutura[0] in globals():
                            if limpesa == estrutura[1]:
                                confirmacao = []
                                for resp_chute in estrutura[1::]:
                                    confirmacao.append(resp_chute)
                                resposta_final = random.randint(2, len(confirmacao))
                                if '$' in estrutura[resposta_final]:
                                    name = msg['from']['first_name']
                                    resposta_ao_telegram = globals()[estrutura[0]](estrutura[resposta_final], name)
                                    bot.sendMessage(chatID, resposta_ao_telegram)
                                    return
                                    # return resposta_ao_telegram
                                else:
                                    # bot.sendMessage(chatID, estrutura[resposta_final])
                                    bot.sendMessage(chatID, estrutura[resposta_final])
                                    return
                        else:
                            bot.sendMessage(chatID, "encontrado entrada no CSV nao permitida!")
        bot.sendMessage(chatID, 'Não sei responder isso ainda!')


def on_callback_query(msg):
    query_id, from_id, query_data = amanobot.glance(msg, flavor='callback_query')
    sos = emojis.encode(":sos:")
    CD = emojis.encode(":minidisc:")
    chat_id = msg['message']['chat']['id']
    click = ''.join(query_data)
    click = click.split(' ')
    bot.answerCallbackQuery(query_id)
    sites = ['https://www.youtube.com/', 'https://www.mercadolivre.com.br/', 'https://open.spotify.com/',
             'https://komoda-eletro-eletronica.webnode.com/']

    if click[0] == 'go':
        bot.sendMessage(chat_id, f"https://www.google.com/search?q={click[1]}")
        bot.sendMessage(chat_id, 'Esta satisfeito com a pesquisa?')
    elif click[0] == 'wiki':
        bot.sendMessage(chat_id, f"https://pt.wikipedia.org/wiki/{click[1]}")
    elif query_data == 'L':
        bot.sendMessage(chat_id, "https://t.me/joinchat/Fj1EnkP5Kpfzs8IrrfPz2Q")
    elif query_data == 'SOS':
        bot.sendMessage(chat_id, 'Para pesquisar digite, ( hall pesquisar + o que deseja pesquisar) e '
                                 'aperte o botão de sua escolha!')
        bot.sendMessage(chat_id, "Digite (hall1 + nome) para receber os usuarios novos \nDigite hall2 "
                                 "para alertar usuarios sobre foto de perfil")
        bot.sendMessage(chat_id, text=sos)
    elif query_data == 'url':
        for i in sites:
            bot.sendMessage(chat_id, text=i)
            sleep(1.50)
        bot.sendMessage(chat_id, 'Esses são os sites mais usados!')
    elif query_data == 'co':
        bot.sendMessage(chat_id, 'Conteúdo:', reply_markup=botao4())
    elif query_data == 'M':
        bot.sendMessage(chat_id, '***OPÇÕES DO MENU CLIQUE***', reply_markup=botao2())
    elif query_data == 'ha':
        bot.sendMessage(chat_id, 'https://anos-80.mp3cielo.com/')
        bot.sendMessage(chat_id, CD)
    elif query_data == 'mu':
        audio = abre_id('ID_music.txt')
        for i in audio[0:15]:
            bot.sendAudio(from_id, audio=i)
        bot.sendMessage(from_id, 'Por enquanto só enviarei esses!')
        bot.sendMessage(chat_id, f"Enviei no seu  privado")

    elif query_data == 'curs':
        bot.sendMessage(chat_id, f"Sem cursos no momento! Procure nos arquivos do grupo que tem varios tutoriais")

    elif query_data == 'li':
        bot.sendMessage(chat_id, f"Sem HQs no momento!")


TOKEN = "771827013:AAFDYw87Xv9pnSGUPLp6H8BLFnf-iu-ANo8"
# TOKEN = "870167339:AAEXvrPJf8NR9GWoOTWUvw-gdeGPy7kDkDE"
bot = amanobot.Bot(TOKEN)
MessageLoop(bot, {'chat': recebendo,
                  'callback_query': on_callback_query}).run_as_thread()

while True:
    sleep(5)
