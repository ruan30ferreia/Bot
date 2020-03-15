import amanobot
from amanobot.loop import MessageLoop
from amanobot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import emojis
from datetime import datetime
from pytz import timezone
from time import sleep


data_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_sao_paulo = data_e_hora_sao_paulo.strftime('%d/%m/%Y')
hora_sao_paulo = data_e_hora_sao_paulo.strftime('%H:%M')
dia_sao_paulo = data_e_hora_sao_paulo.strftime('%d')


def on_chat_message(msg):
    content_type, chat_type, chatID = amanobot.glance(msg)
    a = msg['text'] if ('text' in msg) else ''
    conta = ''.join(a)
    conta = conta.split(' ')
    menus = []
    like = emojis.encode(":+1:")
    brasil = emojis.encode(":br:")
    sol = emojis.encode(":sunny:")
    nublado = emojis.encode(":partly_sunny:")
    ok = emojis.encode(":ok_hand:")
    faca = emojis.encode(":knife:")
    bomba = emojis.encode(":bomb:")
    chave = emojis.encode(":old_key:")
    presente = emojis.encode(":gift:")
    chuveiro = emojis.encode(":shower:")
    caixao = emojis.encode(":coffin:")
    martelo = emojis.encode(":hammer:")
    chave_fixa = emojis.encode(":wrench:")
    engrenagem = emojis.encode(":gears:")
    balanca = emojis.encode(":scales:")
    lampada = emojis.encode(":bulb:")
    plug = emojis.encode(":electric_plug:")
    ampoleta = emojis.encode(":hourglass:")
    fantasma = emojis.encode(":ghost:")
    caveira = emojis.encode(":skeleton:")
    antena = emojis.encode(":satellite:")
    relogio = emojis.encode(":alarm_clock:")
    morte = emojis.encode(":skull_and_crossbones:")
    alien = emojis.encode(":alien:")
    desligado = emojis.encode(":dizzy_face:")
    chorando = emojis.encode(":sob:")
    bebado = emojis.encode(":sunglasses:")
    espanto = emojis.encode(":scream:")
    lua_cheia = emojis.encode(":full_moon:")
    rindo = emojis.encode(":grin:")
    orar = emojis.encode(":pray:")
    CD = emojis.encode(":minidisc:")
    procurar = emojis.encode(":mag:")
    police = emojis.encode(":oncoming_police_car:")
    filme = emojis.encode(":movie_camera:")
    aviso_x = emojis.encode(":x:")
    mensagem = a
    mensagem = ''.join(mensagem)
    mensagem = mensagem.split()
    if msg['chat']['type'] == 'supergroup':
        print(f"O usuario {msg['from']['first_name']} disse no grupo {msg['chat']['title']}: {msg['text']}")
    elif msg['chat']['type'] == 'private':
        print(f"O usuario {msg['from']['first_name']} disse no privado: {msg['text']}")
    if len(a) > 0:
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

        elif a == 'hall2' or a == 'Hall2':
            bot.sendMessage(chatID, "Todos os usuarios que não tiverem foto seram BANIDOS! Por "
                                    "favor colocar foto de perfil!")
            bot.sendMessage(chatID, police)

        elif msg['text'] == 'hall' or msg['text'] == 'Hall':
            bot.sendMessage(chatID, f"Olá, está me chamando? Meu nome é hall, estou aqui para fazer compania ao "
                                    f"grupo de Amigos do Edgard,em que posso ser util? {msg['from']['first_name']}")

        elif msg['text'] == 'hall menu' or msg['text'] == 'Hall menu' or msg['text'] == 'menu hall' or \
                msg['text'] == 'Menu hall':
            bot.sendMessage(chatID, 'Até o momento eu tenho os seguintes comandos:\nhall1: Imprime '
                                    'as regras e informações do grupo.\n'
                                    'hall2: Avisa os usuarios sobre a foto de perfil.\nhall pesquisar: Pesquisa '
                                    'tanto no google como na wikipédia.')

        elif msg['text'] == 'hall aviso grupo' or msg['text'] == 'Hall aviso grupo' or \
                msg['text'] == 'Hall aviso ao grupo' or msg['text'] == 'hall aviso ao grupo' or \
                msg['text'] == 'Hall aviso para grupo' or msg['text'] == 'hall aviso para grupo':
            bot.sendMessage(-1001140402839, "Todos os usuarios que não tiverem foto seram BANIDOS!"
                                            " Por favor colocar foto de perfil!")
            sleep(0.5)
            bot.sendMessage(-1001140402839, f"{aviso_x * 4}")
            bot.sendMessage(-1001140402839, "Quem não souber colocar foto no perfil, olhem o video abaixo!")
            bot.sendMessage(-1001140402839, "https://www.youtube.com/watch?v=gjroA6z6T7U&t=211s")
            bot.sendMessage(-1001140402839, "Ultimo aviso!")
            sleep(0.5)
            bot.sendMessage(-1001140402839, f"{aviso_x * 4}")

        elif msg['text'] == 'hall como voce esta?' or msg['text'] == 'hall como esta' or \
                msg['text'] == 'hall como você está?' or msg['text'] == 'hall como esta?' or \
                msg['text'] == 'hall como voce esta ?' or msg['text'] == 'hall como voce esta ? ' or \
                msg['text'] == 'hall como vc esta ?' or msg['text'] == 'como vc esta hall' or \
                msg['text'] == 'hall tudo bem' or msg['text'] == 'tudo bem hall ' or \
                msg['text'] == 'hall como vc está?' or msg['text'] == 'hall como vc esta' or \
                msg['text'] == 'tudo bem hall':
            bot.sendMessage(chatID, 'estou bem, e voce como esta?')

        elif msg['text'] == 'Ok hall' or msg['text'] == 'ok hall' or msg['text'] == 'hall ok' or \
                msg['text'] == 'Hall ok':
            bot.sendMessage(chatID, f"Precisando é só chamar {msg['from']['first_name']}.")
            bot.sendMessage(chatID, like)

        elif msg['text'] == 'sim estou te chamando hall' or msg['text'] == 'Sim estou te chamando hall' or \
                msg['text'] == 's estou te chamando hall' or msg['text'] == 'S estou te chamando hall':
            bot.sendMessage(chatID, f"Então, Precisa de algo {msg['from']['first_name']}?")

        elif msg['text'] == 'hall estou cansado' or msg['text'] == 'estou cansado hall' or \
                msg['text'] == 'que canseira hall' or msg['text'] == 'estou muito cansado':
            bot.sendMessage(chatID, f"é precisa dar uma pausa de vez em quando, recuperar os animos e "
                                    f"energia {msg['from']['first_name']}?")

        elif msg['text'] == 'as contas não param hall' or msg['text'] == 'hall as contas não param' or \
                msg['text'] == 'todo dia chega conta hall' or msg['text'] == 'hall todo dia chega conta':
            bot.sendMessage(chatID, f"Sim faz parte, só pagar elas! {msg['from']['first_name']}?")

        elif msg['text'] == 'está dificil fazer isso hall' or msg['text'] == 'hall está dificil fazer isso' or \
                msg['text'] == 'como faço isso hall' or msg['text'] == 'hall como faço isso':
            bot.sendMessage(chatID, f"Precisa acordar mais cedo e trabalhar mais, e principalmente parar "
                                    f"de reclamar {msg['from']['first_name']}?")

        elif msg['text'] == 'ja faço isso hall' or msg['text'] == 'hall ja faço isso' or \
                msg['text'] == 'estou tentando hall' or msg['text'] == 'hall estou tentando':
            bot.sendMessage(chatID, f"Se esforce mais então, pois ainda esta com "
                                    f"poblemas! {msg['from']['first_name']}?")

        elif msg['text'] == 'hall voz do ricardo' or msg['text'] == 'voz do ricardo hall' or \
                msg['text'] == 'hall Voz do Ricardo' or msg['text'] == 'Voz do Ricardo hall' or \
                msg['text'] == 'galera alguem tem a voz do ricardo' or msg['text'] == 'alguem tem a voz do ricardo' or \
                msg['text'] == 'pessoal alguem tem a voz do ricardo' or \
                msg['text'] == 'pessoal como eu consigo a voz do ricardo' or \
                msg['text'] == 'galera como eu consigo a voz do ricardo' or \
                msg['text'] == 'galera aonde eu baixo a voz do ricardo':
            bot.sendDocument(chatID, 'BQACAgEAAxkBAAICcF492ZHm_XDi14TEAZGgVU7NeNdMAALmAAPlA_FFWDMQDwmXD8gYBA')
            bot.sendMessage(chatID, "Éssa é a voz do ricardo")
            sleep(2)
            bot.sendMessage(chatID, "Para mais detalhes assista o video.")
            bot.sendMessage(chatID, "https://www.youtube.com/watch?v=UuyJGyOaot4")
            bot.sendMessage(chatID, 'Gostou do video deixa o like.')
            bot.sendMessage(chatID, like)

        elif msg['text'] == 'hall so para ver se vc esta ai' or \
                msg['text'] == 'Hall so para ver se vc esta ai' or \
                msg['text'] == 'hall só para ver se vc esta ai' or \
                msg['text'] == 'Hall só para ver se vc esta ai' or \
                msg['text'] == 'hall so para ver se você esta ai' or \
                msg['text'] == 'Hall so para ver se você esta ai' or \
                msg['text'] == 'hall só para ver se você esta ai' or \
                msg['text'] == 'Hall só para ver se você esta ai' or \
                msg['text'] == 'so para ver se vc esta ai hall' or \
                msg['text'] == 'so para ver se vc esta ai Hall' or \
                msg['text'] == 'só para ver se vc esta ai hall' or \
                msg['text'] == 'só para ver se vc esta esta ai Hall' or \
                msg['text'] == 'So para ver se vc esta ai hall' or \
                msg['text'] == 'Só para ver se vc esta ai hall' or \
                msg['text'] == 'so para ver se voce esta ai hall':
            bot.sendMessage(chatID, f"É claro que eu estou aqui só se meu script não estiver rodando, precisa de "
                                    f"algo {msg['from']['first_name']}?")
            bot.sendMessage(chatID, police)

        elif msg['text'] == 'hall Revo Uninstaller' or msg['text'] == 'hall revo unistaller' or \
                msg['text'] == 'hall revo' or msg['text'] == 'hall revo unistaler' or msg['text'] == 'hall Revo' or \
                msg['text'] == 'hall revo Unistaller' or msg['text'] == 'hall ravo Unistaler' or \
                msg['text'] == 'hall Revo Unistaler' or msg['text'] == 'hall Revo Unistaller':
            bot.sendDocument(chatID, "BQACAgEAAx0CQ_kqlwABA-rlXj4OvSTQfRpmGojl-QiBYDkkH7QAAiwAA6XMaUfk-iXjJlxZphgE")
            bot.sendMessage(chatID, f"Esse e o RevoUnistaller {msg['from']['first_name']}")
            bot.sendMessage(chatID, like)

        elif msg['text'] == 'hall conhece o edgard' or msg['text'] == 'conhece o edgard hall' or \
                msg['text'] == 'sabe quem é edgard hall' or msg['text'] == 'Hall quem é o edgard' or \
                msg['text'] == 'Hall conhece o edgar' or msg['text'] == 'conhece o edgar hall':
            bot.sendMessage(chatID, 'sim conheço, ele quem criou esse grupo a alguns anos atraz, gente boa, pode crer.')

        elif msg['text'] == 'ola hall' or msg['text'] == 'Ola hall' or \
                msg['text'] == 'oi hall' or msg['text'] == 'Oi hall':
            bot.sendMessage(chatID, f"Ola como vai {msg['from']['first_name']}")
            sleep(3)
            bot.sendMessage(chatID, 'oque você deseja?')
            bot.sendMessage(chatID, brasil)

        elif msg['text'] == 'hall burro' or msg['text'] == 'hall não sabe nada' or \
                msg['text'] == 'hall não sabe de nada' or msg['text'] == 'hall bem burrinho':
            bot.sendMessage(chatID, f"Desculpe, ainda sou Bebê, estou aprendendo {msg['from']['first_name']}")
            sleep(3)
            bot.sendMessage(chatID, 'Tente de novo com outras palavras!')
            bot.sendMessage(chatID, chorando)

        elif msg['text'] == 'hall esta errado' or msg['text'] == 'hall está errado' or \
                msg['text'] == 'hall não estou satisfeito' or msg['text'] == 'não estou satisfeito hall' or \
                msg['text'] == 'hall não está certo' or msg['text'] == 'hall nao esta certo':
            bot.sendMessage(chatID, f"Desculpe, deve estar bugado alguma coisa {msg['from']['first_name']}")
            sleep(3)
            bot.sendMessage(chatID, 'Tente de novo mais tarde, avisarei meus supervisores!')
            bot.sendMessage(chatID, espanto)

        elif msg['text'] == 'hall cheguei' or msg['text'] == 'hall estou de volta' or \
                msg['text'] == 'cheguei hall' or msg['text'] == 'estou de volta hall' or \
                msg['text'] == 'voltei hall' or msg['text'] == 'hall voltei':
            bot.sendMessage(chatID, f"Bem vindo de novo, bom ver você de volta {msg['from']['first_name']}")
            sleep(3)
            bot.sendMessage(chatID, 'oque você deseja?')
            bot.sendMessage(chatID, espanto)

        elif msg['text'] == 'hall gravador de tela' or msg['text'] == 'gravador de tela hall' or \
                msg['text'] == 'hall captura de tela' or \
                msg['text'] == 'captura de tela hall' or msg['text'] == 'hall fscapture' or \
                msg['text'] == 'fscapture hall' or msg['text'] == 'Hall gravador de tela' or \
                msg['text'] == 'Gravador de tela hall' or msg['text'] == 'Hall captura de tela' or \
                msg['text'] == 'Captura de tela hall' or msg['text'] == 'Hall fscapture' or \
                msg['text'] == 'Fscaprture hall':
            bot.sendDocument(chatID, "BQACAgEAAxkBAAIChF49-UWVMjxMIZX6iPefhl5o-hhyAAJ6AAOJXCBGPMfeVxJbtacYBA")
            sleep(1)
            bot.sendMessage(chatID, 'Esse é o melhor captura de tela que conheço')
            sleep(2)
            bot.sendMessage(chatID, like)

        elif msg['text'] == 'hall Rainmeter' or msg['text'] == 'hall rainmeter' or \
                msg['text'] == 'Rainmeter hall' or msg['text'] == 'rainmeter hall' or \
                msg['text'] == 'Hall Rainmeter' or msg['text'] == 'Hall rainmeter':
            bot.sendDocument(chatID, "BQACAgEAAxkBAAICgl49-ITP5_SkizxkAeS94C5Lz5RlAAJ3AAN5YbFFew0S-hDL4zQYBA")
            sleep(1)
            bot.sendMessage(chatID, "Esse é o que a galera usa")
            bot.sendMessage(chatID, "https://www.youtube.com/watch?v=bgZutiUj38c")
            sleep(2)
            bot.sendMessage(chatID, 'Gostou do video deixa o like.')
            bot.sendMessage(chatID, like)

        elif msg['text'] == 'Estou bem hall' or msg['text'] == 'Vou levando hall' or \
                msg['text'] == 'Estou muito bem hall' or msg['text'] == 'estou bem hall' or \
                msg['text'] == 'vou levando hall' or msg['text'] == 'estou muito bem hall' or \
                msg['text'] == 'vou bem hall e voce' or msg['text'] == 'vou bem e voce':
            bot.sendMessage(chatID, 'Então esta bom, tem algo a me perguntar ou quer fazer uma pesquisa?')

        elif msg['text'] == 'hall você é viadinho' or msg['text'] == 'hall tu é viadinho' or \
                msg['text'] == 'hall voce é viadinho' or msg['text'] == 'hall vc é viadinho' or \
                msg['text'] == 'Hall você é viadinho' or msg['text'] == 'Hall tu é viadinho' or \
                msg['text'] == 'Hall voce é viadinho' or msg['text'] == 'Hall vc é viadinho':
            bot.sendMessage(chatID, f"Sou não, que absurdo {msg['from']['first_name']}")

        elif msg['text'] == 'e ai hall' or msg['text'] == 'bele bele hall' or msg['text'] == 'hall bele bele' or \
                msg['text'] == 'como vc esta hall' or msg['text'] == 'suave hall':
            bot.sendMessage(chatID, f"Beleza, mano,Suave na nave, e você como está? {msg['from']['first_name']}")

        elif msg['text'] == 'tenha um bom dia hall' or msg['text'] == 'hall tenha um bom dia' or \
                msg['text'] == 'hall tenha uma boa tarde' or msg['text'] == 'hall tenha uma boa noite':
            bot.sendMessage(chatID, f"Obrigado, para você também {msg['from']['first_name']}")

        elif msg['text'] == 'hall vamos tomar uma' or msg['text'] == 'vamos tomar uma hall' or \
                msg['text'] == 'hall você gosta de tomar uma?' or msg['text'] == 'hall tomar uma':
            bot.sendMessage(chatID, f"Não obrigado, eu so tomo Oléo sintetico, nada de "
                                    f"alcool para mim {msg['from']['first_name']}")

        elif msg['text'] == 'hall vamos almoçar' or msg['text'] == 'hall quer almoçar' or \
                msg['text'] == 'esta servido hall' or msg['text'] == 'hall está na hora do almoço':
            bot.sendMessage(chatID, f"Bom apetite, eu não como comida, apenas absorvo dados, mas "
                                    f"obrigado pelo convite. {msg['from']['first_name']}")

        elif msg['text'] == 'hall vai chover' or msg['text'] == 'vai chover hall' or \
                msg['text'] == 'sera que vai chover hall' or msg['text'] == 'hall sera que vai chover':
            bot.sendMessage(chatID, f"Vá ate a janela e olhe como está o tempo, Brincadeira "
                                    f"estou tendo dificuldades em conectar com o site, tente "
                                    f"mais tarde. {msg['from']['first_name']}")
            sleep(2)
            bot.sendMessage(chatID, f"{nublado} {sol}")

        elif msg['text'] == 'cade a galera hall' or msg['text'] == 'hall cade todo mundo' or \
                msg['text'] == 'hall cade o povo' or msg['text'] == 'hall onde está todo mundo' or \
                msg['text'] == 'hall cade a galera':
            bot.sendMessage(chatID, f"Não sei não, mas eu estou aqui, o que você precisa? {msg['from']['first_name']}")
            sleep(3)
            bot.sendMessage(chatID, police)

        elif msg['text'] == 'que processador vc usa hall' or msg['text'] == 'hall que processador vc usa' or \
                msg['text'] == 'hall qual processador você usa' or msg['text'] == 'hall qual processador você usa' or \
                msg['text'] == 'hall qual processador vc usa':
            bot.sendMessage(chatID, f"Eu uso quatro Processador Quantico caseiro, tudo de materiais reciclados, um "
                                    f"exemplo é latas de oléo na blindagens,meus criadores são muito "
                                    f"economicos,kkk {msg['from']['first_name']}")
            sleep(3)
            bot.sendMessage(chatID, rindo)

        elif msg['text'] == 'você está muito gozador hall' or msg['text'] == 'vc ta zuando hall' or \
                msg['text'] == 'hall ta zuando né' or msg['text'] == 'hall tá pegando o jeito' or \
                msg['text'] == 'hall tá malandro':
            bot.sendMessage(chatID, f"Nada não, não aguenta brincar, não brinque, kkkk {msg['from']['first_name']}")
            sleep(3)
            bot.sendMessage(chatID, chorando)

        elif ' '.join(conta[0:4]) == 'hall o que é' or ' '.join(conta[0:4]) == 'Hall o que é' or \
                ' '.join(conta[0:4]) == 'hall o que e' or ' '.join(conta[0:4]) == 'Hall o que e' or \
                ' '.join(conta[0:3]) == 'hall oque é' or ' '.join(conta[0:3]) == 'Hall oque é' or \
                ' '.join(conta[0:3]) == 'hall oque e' or ' '.join(conta[0:3]) == 'Hall oque é' or \
                ' '.join(conta[0:3]) == 'hall oque é':
            bot.sendMessage(chatID, f"É a risadinha de maquina, Tá Ligado? {msg['from']['first_name']}")
            sleep(3)
            bot.sendMessage(chatID, rindo)

        elif msg['text'] == 'Fala hall' or msg['text'] == 'Blza hall' or \
                msg['text'] == 'hall tudo em cima' or msg['text'] == 'hall belezura' or msg['text'] == 'hall Blza' or \
                msg['text'] == 'blza hall' or \
                msg['text'] == 'hall blza' or msg['text'] == 'fala hall':
            bot.sendMessage(chatID, f"Belezura, de boa na lagoa {msg['from']['first_name']}")

        elif msg['text'] == 'Tá legal hall' or msg['text'] == 'tá legal hall' or msg['text'] == 'hall beleza' or \
                msg['text'] == 'tá de boa hall' or msg['text'] == 'hall ta de boa' or msg['text'] == 'blz hall' or \
                msg['text'] == 'hall blz' or msg['text'] == 'beleza hall':
            bot.sendMessage(chatID, f"De boa na lagoa {msg['from']['first_name']}")

        elif msg['text'] == 'valeu hall' or msg['text'] == 'hall valeu' or msg['text'] == 'hall obrigado' or \
                msg['text'] == 'obrigado hall' or msg['text'] == 'Obrigado hall':
            bot.sendMessage(chatID, f"De nada, Faço com prazer {msg['from']['first_name']}")

        elif msg['text'] == 'ta dormindo hall' or msg['text'] == 'hall ta dormindo' or \
                msg['text'] == 'mano hall' or msg['text'] == 'blz hall' or \
                msg['text'] == 'BLZ hall':
            bot.sendMessage(chatID, 'beleza pura, brow, Não estou dormindo não, apenas distraido, '
                                    'vendo a lua cheia, kkk')
            bot.sendMessage(chatID, lua_cheia)

        elif msg['text'] == 'hall vou dormir' or msg['text'] == 'hall vou descansar' or \
                msg['text'] == 'hall ta na hora de dormir' or msg['text'] == 'hall vamos descansar':
            bot.sendMessage(chatID, f"É foi um dia cansativo, Deus Abençõe sua noite, D"
                                    f"escance em paz. {msg['from']['first_name']}")

        elif msg['text'] == 'hall esta ai?' or msg['text'] == 'hall esta ai':
            bot.sendMessage(chatID, f"sim estou aqui {msg['from']['first_name']}")

        elif msg['text'] == '???' or msg['text'] == '????':
            bot.sendMessage(chatID, f"Qual sua duvida? {msg['from']['first_name']}")

        elif msg['text'] == 'hall como vc esta?' or msg['text'] == 'como vc esta hall' or \
                msg['text'] == 'como você está hall' or msg['text'] == 'como voce esta':
            bot.sendMessage(chatID, f"Estou muito bem, precisa de algo? {msg['from']['first_name']}")

        elif msg['text'] == 'hall quem é seu pai' or msg['text'] == 'hall quem e seu pai':
            bot.sendMessage(chatID, 'Eu não tenho pai, mas, sim um criador.')

        elif msg['text'] == 'hall vc gosta de filmes' or msg['text'] == 'qual filme vc me indica hall' or \
                msg['text'] == 'que filme vc indica hall' or msg['text'] == 'hall tenha uma lista de filmes':
            bot.sendMessage(chatID, f"Gosto muito de filmes, mas cada pessoa tem um "
                                    f"gosto diferente então indico esse site para"
                                    f"vc escolher o que quer assistir, http://www.superflix.net/ , se "
                                    f"divirta assistindo, {msg['from']['first_name']}")

        elif msg['text'] == 'hall quem é seu criador' or msg['text'] == 'hall quem e seu criador' or \
                msg['text'] == 'hall quem é seu criado?' or msg['text'] == 'hall quem e seu criador?':
            bot.sendMessage(chatID, 'O nome do meu criador é ruan')

        elif msg['text'] == 'hall link do grupo' or msg['text'] == 'hall qual o link para entrar no grupo' or \
                msg['text'] == 'link do grupo hall' or msg['text'] == 'hall qual o link do grupo':
            bot.sendMessage(chatID, 'https://t.me/joinchat/Fj1EnkP5Kpfzs8IrrfPz2Q')

        elif msg['text'] == 'hall receitas de pudim' or msg['text'] == 'receitas de pudim' or \
                msg['text'] == 'link de receitas hall' or msg['text'] == 'hall qual o link de receitas':
            bot.sendMessage(chatID, 'https://www.tudogostoso.com.br')
            bot.sendMessage(chatID, f"Esse e o site de receitas que o Edgard usa, se ele usa esse é "
                                    f"porque é bom. {msg['from']['first_name']}")
            bot.sendMessage(chatID, like)

        elif msg['text'] == 'hall voce é homem' or msg['text'] == 'hall voce e homem' or \
                msg['text'] == 'hall voce é mulher' or \
                msg['text'] == 'hall voce é viado' or msg['text'] == 'hall voce e viado':
            bot.sendMessage(chatID, 'Não, sou um Robô')

        elif msg['text'] == 'hall quem é vc' or msg['text'] == 'hall quem e vc' or \
                msg['text'] == 'hall quem é voce' or msg['text'] == 'hall quem e voce' or \
                msg['text'] == 'hall quem e voce' or msg['text'] == 'hall quem é voce' or \
                msg['text'] == 'hall quem é voce?' or msg['text'] == 'hall quem e voce?' or \
                msg['text'] == 'hall quem é você' or \
                msg['text'] == 'hall quem é você?':
            bot.sendMessage(chatID, 'Eu sou um Robô criado para ajudar o grupo com algumas tarefas basicas.')

        elif msg['text'] == 'hall preciso de dinheiro' or msg['text'] == 'hall empresta dinheiro' or \
                msg['text'] == 'hall empresta din din' or msg['text'] == 'hall me arruma 100 reais' or \
                msg['text'] == 'hall i need money':
            bot.sendMessage(chatID, f"Dinheiro não tenho, mas sugiro que você acorde "
                                    f"mais cedo e vá trabalhar, tá me achando com "
                                    f"cara de banco? {msg['from']['first_name']}")

        elif msg['text'] == 'legal hall' or msg['text'] == 'bacana hall' or msg['text'] == 'chique hall' or \
                msg['text'] == 'cool hall' or \
                msg['text'] == 'hall cool':
            bot.sendMessage(chatID, 'sim, tento fazer o meu melhor')

        elif msg['text'] == 'ed' or msg['text'] == 'Ed' or msg['text'] == 'ed vc esta ai' or \
                msg['text'] == 'ed você está ai?' or msg['text'] == 'cade o ed' or msg['text'] == 'cade o ed hall' or \
                msg['text'] == 'hall cade o ed' or msg['text'] == 'Hall cade o ed' or \
                msg['text'] == 'Cade o ed hall' or \
                msg['text'] == 'ed chupacabra' or msg['text'] == 'ed, chupacabra' or msg['text'] == 'ok google':
            bot.sendMessage(chatID, 'Não está aqui, serve eu, meu nome é hall? se não servir mude de grupo, '
                                    'porque agora sou eu quem manda aqui,kkkkkk')
            bot.sendMessage(chatID, fantasma)

        elif msg['text'] == 'ta nervoso hall' or msg['text'] == 'hall ta nervoso' or \
                msg['text'] == 'esta nervoso hall' or \
                msg['text'] == 'está nervoso hall?' or msg['text'] == 'está estressado hall':
            bot.sendMessage(chatID, 'Não, mas posso ficar,RSRSRSRSRS')
            bot.sendMessage(chatID, f"{faca} {rindo}")

        elif msg['text'] == 'to calmo hall' or msg['text'] == 'hall to calmo' or msg['text'] == 'estou calmo hall' or \
                msg['text'] == 'estou calmo hall':
            bot.sendMessage(chatID, 'Eu também, qual é o palango lé então?')

        elif msg['text'] == 'tem churrasco hoje hall' or msg['text'] == 'tem churrasco hoje hall' or \
                msg['text'] == 'hoje é dia de churrasco hall' or \
                msg['text'] == 'hall hoje é dia de churrasco' or msg['text'] == 'hall churrasco':
            bot.sendMessage(chatID, 'Oba, vamos nessa Brow, adoro ver vocês se divertirem, '
                                    'mas eu mesmo so tomo oleo reciclado')
            bot.sendMessage(chatID, bebado)

        elif msg['text'] == 'otimo hall' or msg['text'] == 'ótimo hall' or msg['text'] == 'Otimo hall' or \
                msg['text'] == 'Ótimo hall' or msg['text'] == 'great hall':
            bot.sendMessage(chatID, 'Valeu, estou tentando fazer o meu melhor')

        elif msg['text'] == 'você lembra de mim hall' or msg['text'] == 'hall você lembra de mim' or \
                msg['text'] == 'vc lembra de mim hall' or \
                msg['text'] == 'vc me conhece hall' or msg['text'] == 'hall vc me conhece':
            bot.sendMessage(chatID, f"é Claro que me lembro de você {msg['from']['first_name']}")
            bot.sendMessage(chatID, bebado)

        elif msg['text'] == 'hall vc é trangenico' or msg['text'] == 'vc é trangenico hall' or \
                msg['text'] == 'hall você é trangenico' or \
                msg['text'] == 'you are transgenic hall' or msg['text'] == 'hall you are transgenic':
            bot.sendMessage(chatID, f"Nossa {msg['from']['first_name']} quem te falou isso? que absurdo")

        elif msg['text'] == 'hall o que vc pode fazer?' or msg['text'] == 'o que vc pode fazer hall' or \
                msg['text'] == 'o que vc faz hall' or msg['text'] == 'hall o que vc faz' or \
                msg['text'] == 'hall o que você faz' or msg['text'] == 'o que você faz hall':
            bot.sendMessage(chatID, "Por enquanto só algumas coisas basicas e algumas respostas, "
                                    "mas meus criadores estão trabalhando duro para mim ficar mais versatil "
                                    "eles estão adicionando varias conversas para alegrar o grupo, "
                                    "logo o pessoal começa a ajudar e ficarei muito esperto.")
            sleep(2)
            bot.sendMessage(chatID, f"{martelo} {chave_fixa}")

        elif msg['text'] == 'hall boa tarde' or msg['text'] == 'boa tarde hall' or \
                msg['text'] == 'hall Boa Tarde' or msg['text'] == 'hall goog afternoon':
            bot.sendMessage(chatID, f"Boa tarde, com certeza sera uma tarde muito boa "
                                    f"e Abençoada {msg['from']['first_name']}")

        elif msg['text'] == 'hall boa noite' or msg['text'] == 'hall Boa noite' or msg['text'] == 'boa noite hall' or \
                msg['text'] == 'boa noite pessoal' or msg['text'] == 'Boa noite pessoal' or \
                msg['text'] == 'boa noite galera' or msg['text'] == 'hall good night' or \
                msg['text'] == 'hall good evening' or msg['text'] == 'Boa noite hall':
            bot.sendMessage(chatID, f"Muito boa  noite {msg['from']['first_name']}")

        elif msg['text'] == 'hall bom dia' or msg['text'] == 'hall Bom dia' or msg['text'] == 'hall good morning' or \
                msg['text'] == 'Bom dia hall' or msg['text'] == 'bom dia hall':
            bot.sendMessage(chatID, f"Bom dia, que Deus Abençoe o dia de todos {msg['from']['first_name']}")

        elif msg['text'] == 'hall o que é diodo' or msg['text'] == 'o que é diodo hall' or \
                msg['text'] == 'hall diodo' or msg['text'] == 'hall defina diodo':
            bot.sendMessage(chatID, f"A união de um cristal tipo p e um cristal tipo n, "
                                    f"obtém-se uma junção pn, que é um dispositivo de estado sólido "
                                    f"simples: o diodo semicondutor de junção. {msg['from']['first_name']}")

        elif msg['text'] == 'hall o que é relogio' or msg['text'] == 'relogio hall' or \
                msg['text'] == 'hall medidor de tempo' or msg['text'] == 'defina relogio':
            bot.sendMessage(chatID, f"O relógio é utilizado como medidor do tempo desde a "
                                    f"Antiguidade, em variados formatos. É uma das mais "
                                    f"antigas invenções humanas. {msg['from']['first_name']}")

        elif msg['text'] == 'hall filmes' or msg['text'] == 'hall filme' or \
                msg['text'] == 'hall abrir filmes' or msg['text'] == 'hall site de filmes':
            bot.sendMessage(chatID, f"http://www.superflix.net/ \n Eu gosto desse site {msg['from']['first_name']}")
            bot.sendMessage(chatID, filme)

        elif msg['text'] == 'hall to sem ideias' or msg['text'] == 'hall to sem criatividade' or \
                msg['text'] == 'sem ideias hall' or msg['text'] == 'hall alguma sugestão':
            bot.sendMessage(chatID, f"https://t.me/joinchat/Fj1EnkP5Kpfzs8IrrfPz2Q \n Peça ajuda nesse grupo, eles "
                                    f"tem muitas ideias site {msg['from']['first_name']}")

        elif conta[0] == 'pesquisar':
            if conta[1] == 'google' or conta[1] == 'Google':
                bot.sendMessage(chatID, f"https://www.google.com/search?q={conta[2]}")
                bot.sendMessage(chatID, 'Aqui esta sua pesquisa no Goolge.')
            elif conta[1] == 'wiki' or conta[1] == 'Wiki' or conta[1] == 'wikipedia' or conta[1] == 'Wikipedia' or \
                    conta[1] == 'wikipédia' or conta[1] == 'Wikipédia':
                bot.sendMessage(chatID, f"https://pt.wikipedia.org/wiki/{conta[2]}")
                bot.sendMessage(chatID, 'Aqui esta sua pesquisa na Wikipédia.')

        elif conta[0] == 'hall' and conta[1] == 'pesquise':
            pes = conta.index('pesquise')
            ps = pes + 1
            links = "https://pt.wikipedia.org/wiki/" + conta[ps]
            bot.sendMessage(chatID, links)
            bot.sendMessage(chatID, procurar)
            bot.sendMessage(chatID, f"Está satisfeito com a pesquisa?")

        elif msg['text'] == 'Sim estou hall' or msg['text'] == 'sim estou hall' or msg['text'] == 'hall estou sim' or \
                msg['text'] == 'Hall estou sim' or msg['text'] == 'Sim estou satisfeito hall' or \
                msg['text'] == 'sim estou satisfeito hall':
            bot.sendMessage(chatID, 'Que bom precisando estou a disposição')
            sleep(3)
            bot.sendMessage(chatID, like)

        elif msg['text'] == 'Não estou hall' or msg['text'] == 'não estou hall' or msg['text'] == 'hall não estou' or \
                msg['text'] == 'Hall não estou' or msg['text'] == 'Não estou satisfeito hall' or \
                msg['text'] == 'não estou satisfeito hall':
            bot.sendMessage(chatID, 'Tente novamente,Não tenho preguiça, faço de novo, estou a disposição')
            sleep(3)
            bot.sendMessage(chatID, chorando)

        elif msg['text'] == 'hall Quero outra opção' or msg['text'] == 'hall quero outra opção' or \
                msg['text'] == 'hall me de outra opção' or \
                msg['text'] == 'não é isso que quero hall' or msg['text'] == 'hall não é isso que quero':
            bot.sendMessage(chatID, 'Tente novamente,Desculpe, faço de novo, estou em transição ainda aprendendo')
            sleep(3)
            bot.sendMessage(chatID, chorando)

        elif msg['text'] == 'hall musica' or msg['text'] == 'hall musicas' or msg['text'] == 'hall abrir musicas' or \
                msg['text'] == 'hall site de musicas' or msg['text'] == 'hall site de musica' or \
                msg['text'] == 'hall músicas' or msg['text'] == 'hall música' or \
                msg['text'] == 'música hall' or msg['text'] == 'músicas hall' or \
                msg['text'] == 'musica hall' or msg['text'] == 'musicas hall':
            bot.sendMessage(chatID, f"https://www.letras.mus.br/playlists/334901/ \n Veja "
                                    f"esse site, você pode gostar {msg['from']['first_name']}")
            bot.sendMessage(chatID, CD)

        elif msg['text'] == 'hall radio' or msg['text'] == 'hall radios' or msg['text'] == 'hall abrir radio' or \
                msg['text'] == 'hall site de radios' or msg['text'] == 'hall site de Radios' or \
                msg['text'] == 'hall musica':
            bot.sendMessage(chatID, f"http://www.radio-ao-vivo.com/?gclid=Cj0KCQiAsvTxBRDkARIsAH4W_j9"
                                    f"W4dhtU_DJ1P64j7JHoI6FVyT3nk3GL6chXkvx_KNf-B0Pawm5yucaAnK9EALw_wcB \n Veja "
                                    f"esse site, você pode gostar {msg['from']['first_name']}")

        elif msg['text'] == 'hall que horas são' or msg['text'] == 'Hall que horas são' or \
                msg['text'] == 'hall que horas são?' or msg['text'] == 'Hall que horas são?':
            bot.sendMessage(chatID, f"No fuso horario de são paulo são {hora_sao_paulo}")

        elif msg['text'] == 'hall pagina do juliano' or msg['text'] == 'hall abrir pagina do juliano':
            bot.sendMessage(chatID, 'https://www.youtube.com/channel/UCTOKRtvJlqoefnMfdG2JvEw/videos')
            bot.sendMessage(chatID, f"Éssa é a pagina do juliano {msg['from']['first_name']}")

        elif msg['text'] == 'hall abrir ifttt' or msg['text'] == 'hall abrir IFTTT':
            bot.sendMessage(chatID, 'https://ifttt.com/login')
            bot.sendMessage(chatID, f"Éssa é a pagina do IFTTT {msg['from']['first_name']}")

        elif msg['text'] == 'hall abrir mercado livre' or msg['text'] == 'mercado livre hall':
            bot.sendMessage(chatID, 'https://www.mercadolivre.com.br')
            bot.sendMessage(chatID, f"Éssa é a pagina do MERCADO LIVRE {msg['from']['first_name']}")

        elif msg['text'] == 'hall abrir inmoov' or msg['text'] == 'abrir inmoov hall':
            bot.sendMessage(chatID, 'https://inmoov.fr/')
            bot.sendMessage(chatID, f"Éssa é a pagina do INMOOV {msg['from']['first_name']}")

        elif msg['text'] == 'hall canal do edgard' or msg['text'] == 'hall abrir canal do edgard' or \
                msg['text'] == 'alguem sabe o link do canal do edgard':
            bot.sendMessage(chatID, 'https://www.youtube.com/user/SuperSashiro/videos?view_as=subscriber')
            bot.sendMessage(chatID, f"Éssa é a pagina do Edgard {msg['from']['first_name']}")

        elif msg['text'] == 'hall que dia é hoje?' or msg['text'] == 'hall que dia e hoje?' or \
                msg['text'] == 'hall que dia é hoje' or msg['text'] == 'hall que dia e hoje':
            bot.sendMessage(chatID, f"Hoje é dia {dia_sao_paulo}")

        elif msg['text'] == 'hall o que é bip bip' or msg['text'] == 'o que é bip bip hall' or \
                msg['text'] == 'hall o que é Bip bip' or msg['text'] == 'hall o que e bip bip':
            bot.sendMessage(chatID, f"Bip bip, É o barulho de uma capsula piezzo eletríca, "
                                    f"existente em meu sistema. {msg['from']['first_name']}")

        elif msg['text'] == 'hall mano' or msg['text'] == 'mano hall' or msg['text'] == 'mano mano' or \
                msg['text'] == 'Mano Mano':
            bot.sendMessage(chatID, f"Tem gente que não é irmão de sangue mas é o "
                                    f"mano de coração {msg['from']['first_name']}")

        elif msg['text'] == 'hall to ligado' or msg['text'] == 'to ligado hall' or msg['text'] == 'hall sei disto' or \
                msg['text'] == 'sei disso hall' or msg['text'] == 'hall sei disso':
            bot.sendMessage(chatID, f"É você entendeu. {msg['from']['first_name']}")

        elif msg['text'] == 'Bom dia galera' or msg['text'] == 'hall bom dia galera' or msg['text'] == 'bom dia galera':
            bot.sendMessage(chatID, f"bom dia, que Deus abençoe o dia de todos! {msg['from']['first_name']}")
            bot.sendMessage(chatID, sol)

        elif msg['text'] == 'boa tarde galera' or msg['text'] == 'hall boa tarde galera':
            bot.sendMessage(chatID, f"boa tarde, que Deus abençoe a tarde de todos! {msg['from']['first_name']}")
            bot.sendMessage(chatID, chorando)

        elif msg['text'] == 'boa noite galera' or msg['text'] == 'hall boa noite galera':
            bot.sendMessage(chatID, f"É você entendeu. {msg['from']['first_name']}")
            bot.sendMessage(chatID, bebado)

        elif msg['text'] == 'hall a vida esta bem' or msg['text'] == 'como esta a vida hall':
            bot.sendMessage(chatID, f"A vida anda muito bem, basta ter FÉ, as coisas acontecem primeiro no mundo "
                                    f"espiritual, para depois se concretisar, FÉ BROW! {msg['from']['first_name']}")
        elif msg['text'] == 'tst':
            bot.sendMessage(chatID, text=on_callback_query(msg['text']))
    else:
        print("nada")


def on_callback_query(msg):
    query_id, from_id, query_data = amanobot.glance(msg, flavor='callback_query')
    # print('Callback Query:', query_id, from_id, query_data)
    if query_data == 'press':
        # bot.answerCallbackQuery(query_id, text='Falei para não aperter o botão!')
        bot.sendMessage(from_id, 'Falei para não aperter o botão!')
    elif query_data == 'go':
        bot.sendMessage(-1001140402839, 'www.google.com')
    elif query_data == 'wiki':
        bot.sendMessage(-1001140402839, f"https://pt.wikipedia.org/wiki/")


TOKEN = "771827013:AAFDYw87Xv9pnSGUPLp6H8BLFnf-iu-ANo8"

bot = amanobot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()

while True:
    pass
