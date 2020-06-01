# -*- coding: utf-8 -*-
import amanobot
from amanobot.loop import MessageLoop
import emojis
from time import sleep
import random
from bot_pack.buttonFunction import *
from bot_pack.messageHandling import ABC
from bot_pack.textModifiers import *
from bot_pack.timeNow import *


def soma(estrutura, name):
    return estrutura.replace("$", name)


audio = abre_id('ID_music.txt')


def recebendo(msg):
    chatID = msg['chat']['id']
    a = msg['text'] if ('text' in msg) else ''
    conta = a.split()
    letras_mens = list(a)
    aviso_x = emojis.encode(":x:")
    risadinha = emojis.encode(":joy:")
    name = msg['from']['first_name']
    if 'new_chat_member' in msg:
        if 'last_name' in msg:
            bot.sendMessage(chatID, f"Seja bem vindo {msg['new_chat_member']['first_name']} "
                                    f"{msg['new_chat_member']['last_name']} "
                                    f"veja os videos e escute os audios , e "
                                    "principalmente coloque uma foto e nome validos , para  a nossa e sua "
                                    "segurança e também não ser banido pelo robo do grupo, vc vendo os videos "
                                    "saberá como aproveitar os arquivos e musicas do grupo com muito mais "
                                    "facilidade, Siga as regras que são poucas, compartilhe o maximo de arquivos "
                                    "que tiver, isso ajuda a todos, obrigado."
                                    " ———————————————————————————————————————————————————————————-   "
                                    "watch the videos and listen to the audios, and especially put a "
                                    "valid photo and name, for ours and your safety and also not be "
                                    "banned by the group robot, u watching the videos will know how to "
                                    "enjoy the files and music. of the group much easier, follow the few "
                                    "rules, share as many files as you have, it helps everyone, thanks.")
        else:
            bot.sendMessage(chatID, f"Seja bem vindo {msg['new_chat_member']['first_name']} "
                                    f"veja os videos e escute os audios , e "
                                    "principalmente coloque uma foto e nome validos , para  a nossa e sua "
                                    "segurança e também não ser banido pelo robo do grupo, vc vendo os videos "
                                    "saberá como aproveitar os arquivos e musicas do grupo com muito mais "
                                    "facilidade, Siga as regras que são poucas, compartilhe o maximo de arquivos "
                                    "que tiver, isso ajuda a todos, obrigado."
                                    " ———————————————————————————————————————————————————————————-   "
                                    "watch the videos and listen to the audios, and especially put a "
                                    "valid photo and name, for ours and your safety and also not be "
                                    "banned by the group robot, u watching the videos will know how to "
                                    "enjoy the files and music. of the group much easier, follow the few "
                                    "rules, share as many files as you have, it helps everyone, thanks.")
        bot.sendVoice(chatID, 'AwACAgEAAxkBAANVXiuxhUE0WgJDyqj4AAG4eM8254ZiAAI0AAPnWOhEAQg3hqI1xhQYBA')
        bot.sendVoice(chatID, 'AwACAgEAAxkBAANlXiu4q4yzXzfJe6tBjArmNKjYaUYAAlwAA-dY4ETHWLuPWrOryBgE')
        bot.sendVoice(chatID, 'AwACAgEAAxkBAANmXiu4zd9JaawsvLFD4wnEQI9xuBwAAl8AA-dY4EQwetjYNiG1eRgE')
        bot.sendMessage(chatID, 'https://www.youtube.com/watch?v=gjroA6z6T7U&t=211s')
        bot.sendMessage(chatID, 'https://www.youtube.com/watch?v=RZAYppEvkqM&t=80s')
        bot.sendMessage(chatID, "https://www.youtube.com/watch?v=UuyJGyOaot4")

    elif len(a) > 0:
        limpesa = ABC(msg['text'])
        if 'hall' in limpesa:
            if limpesa == 'hall menu' or limpesa == 'menu hall':
                bot.sendMessage(chatID, "***OPÇÕES DO MENU CLIQUE***", reply_markup=botao2())

            elif limpesa == 'hall2':
                bot.sendMessage(chatID, "Todos os usuarios que não tiverem foto seram BANIDOS! Por "
                                        "favor colocar foto de perfil!")
            elif limpesa == 'hall que horas sao' or limpesa == 'que horas sao hall' or \
                    limpesa == 'hall que hora e' or limpesa == 'hall que horas e':
                bot.sendMessage(chatID, f"Agora é {hour()}")

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
                # with open('centralMessages.txt', 'r', encoding='utf-8') as file:
                #     for frase_pv in file:
                #         frase_pv = frase_pv.replace('\n', '')
                #         estrutura = frase_pv.split(':')
                #         if len(estrutura) == 2:
                #             resposta_ao_telegram = estrutura[1]
                #             if limpesa == estrutura[1]:
                #                 bot.sendMessage(chatID, resposta_ao_telegram)
                #         elif len(estrutura) >= 3:
                #             if estrutura[0] in globals():
                #                 if limpesa == estrutura[1]:
                #                     confirmacao = []
                #                     for resp_chute in estrutura[1::]:
                #                         confirmacao.append(resp_chute)
                #                     resposta_final = random.randint(2, len(confirmacao))
                #                     if '$' in estrutura[resposta_final]:
                #                         resposta_ao_telegram = globals()[estrutura[0]](estrutura[resposta_final], name)
                #                         bot.sendMessage(chatID, resposta_ao_telegram)
                #                     else:
                #                         bot.sendMessage(chatID, estrutura[resposta_final])
                #             else:
                #                 print("encontrado entrada no CSV nao permitida!")
                with open('centralMessages.txt', 'r', encoding='utf-8') as file:
                    for frase_pv in file:
                        frase_pv = frase_pv.replace('\n', '')
                        estrutura = frase_pv.split(':')
                        if len(estrutura) == 2:
                            resposta_ao_telegram = estrutura[1]
                            if limpesa == estrutura[1]:
                                bot.sendMessage(chatID, resposta_ao_telegram)
                                return
                                # return resposta_ao_telegram
                        elif len(estrutura) >= 3:
                            if estrutura[0] in globals():
                                if limpesa == estrutura[1]:
                                    confirmacao = []
                                    for resp_chute in estrutura[1::]:
                                        confirmacao.append(resp_chute)
                                    resposta_final = random.randint(2, len(confirmacao))
                                    if '$' in estrutura[resposta_final]:
                                        resposta_ao_telegram = globals()[estrutura[0]](estrutura[resposta_final], 'Ruan')
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
        for i in audio[0:15]:
            bot.sendAudio(from_id, audio=i)
        bot.sendMessage(from_id, 'Por enquanto só enviarei esses!')
        bot.sendMessage(chat_id, f"Enviei no seu  privado")

    elif query_data == 'curs':
        bot.sendMessage(chat_id, f"Sem cursos no momento! Procure nos arquivos do grupo que tem varios tutoriais")

    elif query_data == 'li':
        bot.sendMessage(chat_id, f"Sem HQs no momento!")


# TOKEN = "771827013:AAFDYw87Xv9pnSGUPLp6H8BLFnf-iu-ANo8"
TOKEN = "870167339:AAEXvrPJf8NR9GWoOTWUvw-gdeGPy7kDkDE"
bot = amanobot.Bot(TOKEN)
MessageLoop(bot, {'chat': recebendo,
                  'callback_query': on_callback_query}).run_as_thread()

while True:
    sleep(5)
