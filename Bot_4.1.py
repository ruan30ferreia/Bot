# -*- coding: utf-8 -*-
import amanobot
from amanobot.loop import MessageLoop
from amanobot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import emojis
from time import sleep
from datetime import datetime
from pytz import timezone


abecedario = {'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'Á': 'a', 'À': 'a', 'Â': 'a', 'Ã': 'a', 'é': 'e', 'è': 'e',
              'ê': 'e', 'È': 'e', 'É': 'e', 'Ê': 'e', 'í': 'i', 'ì': 'i', 'î': 'i', 'Ì': 'i', 'Í': 'i', 'Î': 'i',
              'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'Ò': 'o', 'Ó': 'o', 'Ô': 'o', 'Õ': 'o', 'ú': 'u',
              'ù': 'u', 'û': 'u', 'Ù': 'u', 'Ú': 'u', 'Û': 'u', 'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e',
              'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o',
              'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y',
              'Z': 'z'}
lista_acentos = ['`', '´', '~', '^', '?', '!']
abecedario_1 = ['á', 'à', 'â', 'ã', 'À', 'Á', 'Â', 'Ã', 'é', 'è', 'ê', 'È', 'É', 'Ê', 'í', 'ì', 'î', 'Ì', 'Í', 'Î',
                'ó', 'ò', 'ô', 'õ', 'Ò', 'Ó', 'Ô', 'Õ', 'ú', 'ù', 'û', 'Ù', 'Ú', 'Û']
data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_sao_paulo = data_e_hora_sao_paulo.strftime('%d/%m/%Y')
hora_sao_paulo = data_e_hora_sao_paulo.strftime('%H:%M')
dia_sao_paulo = data_e_hora_sao_paulo.strftime('%d')


def botao1(tt=None):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Google', callback_data=f'go {tt}'),
         InlineKeyboardButton(text='Wikipédia', callback_data=f'wiki {tt}')],
    ])
    return keyboard


def botao2():
    menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Link do grupo', callback_data='L'),
         InlineKeyboardButton(text='Help', callback_data='SOS')],
        [InlineKeyboardButton(text='Sites + usados', callback_data='url')],
        [InlineKeyboardButton(text='Conteúdo', callback_data='co')],
    ])
    return menu


def botao3():
    redi = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Menu', callback_data='M')],
    ])
    return redi


def botao4():
    conte = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Cursos', callback_data='curs'),
         InlineKeyboardButton(text='Livros', callback_data='li')],
        [InlineKeyboardButton(text='Musicas', callback_data='mu')],
        [InlineKeyboardButton(text='Radios', callback_data='ha')],
    ])
    return conte


def abrir_resposta():
    with open('resposta.txt', 'r') as ar:
        b = []
        ar.seek(0)
        for be in ar.readlines():
            b.append(be)
        lista_formated1 = list(map(lambda l: l.replace('\n', ''), b))
        return lista_formated1


def testeFile(file_name, limpesa):
    try:
        with open(file_name + '.txt', 'r') as file_verifi:
            for frase_pv in file_verifi:
                camp1, camp2 = frase_pv.split(':')
                if camp1 == limpesa:
                    return 'contem'
                return 'não contem'
    except:
        return 'failed'


def ABC(frase):
    letras_frase = list(frase)
    # palavras_frase = frase.split()
    for i in abecedario:
        while i in letras_frase:
            if i in letras_frase:
                num = letras_frase.index(i)
                letras_frase.pop(num)
                letras_frase.insert(num, abecedario[i])
    for acen in lista_acentos:
        while acen in letras_frase:
            if acen in letras_frase:
                num_1 = letras_frase.index(acen)
                letras_frase.pop(num_1)
    reformado_1 = ''.join(letras_frase)
    palavra_frase = reformado_1.split()
    for pala in palavra_frase:
        if pala == 'vc':
            seque = palavra_frase.index('vc')
            palavra_frase.pop(seque)
            palavra_frase.insert(seque, 'voce')
    reformado = ' '.join(palavra_frase)
    return reformado


def abre_id(arq):
    with open(arq, 'r') as lei:
        z = []
        # print(file.readlines())
        lei.seek(0)
        for le in lei.readlines():
            z.append(le)
        # lista_formated = list(map(lambda l: l.replace('\n', ''), a))
        lista_formated_1 = list(map(lambda l: l.rstrip(), z))
        return lista_formated_1


audio = abre_id('id.txt')


def recebendo(msg):
    chatID = msg['chat']['id']
    a = msg['text'] if ('text' in msg) else ''
    conta = a.split()
    letras_mens = list(a)
    aviso_x = emojis.encode(":x:")
    risadinha = emojis.encode(":joy:")
    name = msg['from']['first_name']
    if len(a) > 0:
        limpesa = ABC(msg['text'])
        if conta[0] == 'hall1' or conta[0] == 'Hall1':
            bot.sendMessage(chatID, f"Seja bem vindo {conta[1]} {conta[2] if len(conta) >= 3 else ''}, "
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
                
        elif limpesa == 'hall menu':
            bot.sendMessage(chatID, "***OPÇÕES DO MENU CLIQUE***", reply_markup=botao2())

        elif limpesa == 'hall2':
            bot.sendMessage(chatID, "Todos os usuarios que não tiverem foto seram BANIDOS! Por "
                                    "favor colocar foto de perfil!")
        elif limpesa == 'hall que horas sao' or limpesa == 'que horas sao hall' or \
                limpesa == 'hall que hora e' or limpesa == 'hall que horas e':
            bot.sendMessage(chatID, f"Agora é {hora_sao_paulo}")

        elif limpesa == 'hall que dia e hoje' or limpesa == 'que dia e hoje hall':
            bot.sendMessage(chatID, f"Hoje é dia {dia_sao_paulo}")

        elif conta[0] == '+' or conta[0] == '+':
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

        elif letras_mens.count('k') > 4:
            bot.sendMessage(chatID, f"Qual a graça, {msg['from']['first_name']} ?")
            bot.sendMessage(chatID, text=risadinha)

        elif letras_mens.count('?') > 3:
            bot.sendMessage(chatID, f"Qual a duvida,posso ajudar {msg['from']['first_name']}?")

        else:
            checagem_file = testeFile(name, limpesa)
            if checagem_file == 'contem':
                with open(name + '.txt', 'r', encoding="UTF8") as conv_pv:
                    for frase_pv in conv_pv:
                        camp1, camp2 = frase_pv.split(':')
                        if camp1 == limpesa:
                            bot.sendMessage(chatID, camp2)
            else:
                with open('hall_txt_novo.txt', 'r', encoding="UTF8") as cvr:
                    for frases_central in cvr:
                        campo1, campo2 = frases_central.split(':')
                        if campo1 == limpesa:
                            bot.sendMessage(chatID, campo2)
    else:
        print('nenhum texto!')


def on_callback_query(msg):
    query_id, from_id, query_data = amanobot.glance(msg, flavor='callback_query')
    sos = emojis.encode(":sos:")
    CD = emojis.encode(":minidisc:")
    chat_id = msg['message']['chat']['id']
    name = msg['message']['from']['first_name']
    click = ''.join(query_data)
    click = click.split(' ')
    bot.answerCallbackQuery(query_id)
    sites = ['https://www.youtube.com/', 'https://www.mercadolivre.com.br/', 'https://open.spotify.com/',
             'https://pagseguro.uol.com.br/', 'https://www.netflix.com/br/', 'http://www.superflix.net/',
             'https://www.thingiverse.com/explore/newest/3d-printing', 'https://komoda-eletro-eletronica.webnode.com/',
             'https://ifttt.com/discover', 'https://blynk.io/en/getting-started']
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
        bot.sendMessage(chat_id, 'Por enquanto eu só conheço esses sites!')
    elif query_data == 'co':
        bot.sendMessage(chat_id, 'Conteúdo:', reply_markup=botao4())
    elif query_data == 'M':
        bot.sendMessage(chat_id, '***OPÇÕES DO MENU CLIQUE***', reply_markup=botao2())
    elif query_data == 'ha':
        bot.sendMessage(chat_id, 'https://anos-80.mp3cielo.com/')
        bot.sendMessage(chat_id, CD)
    elif query_data == 'mu':
        for i in audio[0:51]:
            bot.sendAudio(from_id, audio=i)
        bot.sendMessage(from_id, 'Por enquanto só enviarei esses!')
        bot.sendMessage(chat_id, f"Enviei no seu privado {name}")
        
    elif query_data == 'curs':
        bot.sendMessage(chat_id, f"Sem cursos no momento!")

    elif query_data == 'li':
        bot.sendMessage(chat_id, 'Ainda não tenho livros adicionados aqui!')


# TOKEN = "771827013:AAFDYw87Xv9pnSGUPLp6H8BLFnf-iu-ANo8"
TOKEN = "870167339:AAEXvrPJf8NR9GWoOTWUvw-gdeGPy7kDkDE"
bot = amanobot.Bot(TOKEN)
MessageLoop(bot, {'chat': recebendo,
                  'callback_query': on_callback_query}).run_as_thread()

while True:
    sleep(5)
